from flask import Flask, render_template, request, send_file
import pickle
import numpy as np
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
import io
from datetime import datetime

app = Flask(__name__)

# ---------------- LOAD MODELS ----------------
heart_model = pickle.load(open('models/heart_model.pkl', 'rb'))
diabetes_model = pickle.load(open('models/diabetes_model.pkl', 'rb'))

# ---------------- DATA ----------------
disease_doctor_map = {
    "High Risk of Heart Disease": "Cardiologist",
    "Low Risk of Heart Disease": "General Physician",
    "Diabetic": "Endocrinologist",
    "Not Diabetic": "General Physician"
}

doctors = [
    {"id": 1, "name": "Dr. Rahul Sharma", "specialization": "Cardiologist", "slots": ["10:00 AM", "11:00 AM", "2:30 PM"], "avatar": "👨‍⚕️", "exp": "10 Years Exp.", "hours": "10AM - 2PM", "desc": "Specializes in interventional cardiology and heart failure management."},
    {"id": 2, "name": "Dr. Amit Verma", "specialization": "Cardiologist", "slots": ["1:00 PM", "3:00 PM", "6:00 PM"], "avatar": "👨‍⚕️", "exp": "15 Years Exp.", "hours": "1PM - 6PM", "desc": "Expert in cardiovascular diseases and bypass surgery."},
    {"id": 3, "name": "Dr. Priya Mehta", "specialization": "Endocrinologist", "slots": ["9:00 AM", "12:00 PM", "2:45 PM"], "avatar": "👩‍⚕️", "exp": "8 Years Exp.", "hours": "1PM - 5PM", "desc": "Expert in diabetes management, thyroid disorders and metabolic diseases."},
    {"id": 4, "name": "Dr. Sneha Kapoor", "specialization": "General Physician", "slots": ["4:00 PM", "6:00 PM", "7:25 PM"], "avatar": "👩‍⚕️", "exp": "6 Years Exp.", "hours": "4PM - 7PM", "desc": "Holistic general medicine for routine checkups and chronic condition monitoring."},
    {"id": 5, "name": "Dr. Surendra H V", "specialization": "Endocrinologist", "slots": ["1:00 PM", "5:00 PM"], "avatar": "👨‍⚕️", "exp": "12 Years Exp.", "hours": "1PM - 5PM", "desc": "Senior endocrinologist specializing in insulin resistance and Type 2 Diabetes."},
    {"id": 6, "name": "Dr. Kavita Singh", "specialization": "Endocrinologist", "slots": ["10:00 AM", "2:00 PM"], "avatar": "👩‍⚕️", "exp": "10 Years Exp.", "hours": "10AM - 2PM", "desc": "Specialist in gestational diabetes and hormonal imbalances."}
]

appointments = []

# ---------------- ROUTES ----------------

@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/heart')
def heart():
    return render_template('heart.html')

@app.route('/heart_form')
def heart_form():
    return render_template('heart_form.html')

@app.route('/diabetes')
def diabetes():
    return render_template('diabetes.html')

@app.route('/diabetes_form')
def diabetes_form():
    return render_template('diabetes_form.html')

@app.route('/appointment')
def appointment():
    dept = request.args.get('dept', 'all')
    if dept == 'heart':
        filtered_doctors = [d for d in doctors if d['specialization'] in ['Cardiologist', 'General Physician']]
    elif dept == 'diabetes':
        filtered_doctors = [d for d in doctors if d['specialization'] in ['Endocrinologist', 'General Physician']]
    else:
        filtered_doctors = doctors
    return render_template('appointment.html', doctors=filtered_doctors)

# ---------------- PREDICTION LOGIC ----------------

@app.route('/predict_heart', methods=['POST'])
def predict_heart():
    try:
        features = [float(x) for x in request.form.values()]
        final_input = np.array([features])

        prediction = heart_model.predict(final_input)[0]

        result = "High Risk of Heart Disease" if prediction == 1 else "Low Risk of Heart Disease"

        doctor_type = disease_doctor_map.get(result, "General Physician")
        suggested_doctors = [doc for doc in doctors if doc["specialization"] == doctor_type]

        return render_template(
            'result.html',
            result=result,
            doctor_type=doctor_type,
            doctors=suggested_doctors
        )

    except Exception as e:
        return f"Error: {e}"


@app.route('/predict_diabetes', methods=['POST'])
def predict_diabetes():
    try:
        features = [float(x) for x in request.form.values()]
        final_input = np.array([features])

        prediction = diabetes_model.predict(final_input)[0]

        result = "Diabetic" if prediction == 1 else "Not Diabetic"

        doctor_type = disease_doctor_map.get(result, "General Physician")
        suggested_doctors = [doc for doc in doctors if doc["specialization"] == doctor_type]

        return render_template(
            'result.html',
            result=result,
            doctor_type=doctor_type,
            doctors=suggested_doctors
        )

    except Exception as e:
        return f"Error: {e}"

# ---------------- BOOKING & DASHBOARDS ----------------

@app.route('/book', methods=['POST'])
def book():
    doctor_id = int(request.form.get("doctor_id"))
    slot = request.form.get("slot")
    patient_name = request.form.get("patient_name", "Anonymous User")
    patient_age = request.form.get("age", "N/A")
    issue = request.form.get("issue", "General checkup")

    selected_doctor = next((d for d in doctors if d["id"] == doctor_id), None)

    new_appointment = {
        "id": len(appointments) + 1,
        "doctor_id": doctor_id,
        "doctor_name": selected_doctor["name"],
        "doctor_specialization": selected_doctor["specialization"],
        "patient_name": patient_name,
        "patient_age": patient_age,
        "issue": issue,
        "slot": slot,
        "status": "Pending",
        "date": datetime.now().strftime("%B %d, %Y")
    }

    appointments.append(new_appointment)

    return render_template(
        "confirmation.html",
        doctor_name=selected_doctor["name"],
        slot=slot
    )


@app.route('/user_dashboard')
def user_dashboard():
    return render_template(
        'user_dashboard.html',
        user_appointments=appointments
    )


@app.route('/doctor_dashboard')
def doctor_dashboard():
    return render_template(
        'doctor_dashboard.html',
        all_appointments=appointments
    )


@app.route('/update_status/<int:appt_id>/<string:new_status>')
def update_status(appt_id, new_status):
    appt = next((a for a in appointments if a["id"] == appt_id), None)

    if appt:
        appt["status"] = new_status

    return doctor_dashboard()


# ---------------- DOWNLOAD RECEIPT ----------------

@app.route('/download_receipt')
def download_receipt():
    appt_id = request.args.get('id', type=int)
    if appt_id:
        appt = next((a for a in appointments if a["id"] == appt_id), None)
    else:
        appt = appointments[-1] if appointments else None

    if not appt:
        return "No appointment found!"

    doc = Document()

    # Set Margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.5)
        section.bottom_margin = Inches(0.5)
        section.left_margin = Inches(0.7)
        section.right_margin = Inches(0.7)

    # Header
    header_para = doc.add_paragraph()
    header_para.alignment = WD_ALIGN_PARAGRAPH.CENTER

    run = header_para.add_run("CAREPULSE AI - DIGITAL HEALTH PORTAL")
    run.font.size = Pt(22)
    run.font.bold = True
    run.font.color.rgb = RGBColor(10, 110, 138)

    hospital_info = doc.add_paragraph()
    hospital_info.alignment = WD_ALIGN_PARAGRAPH.CENTER

    hospital_info.add_run(
        "CarePulse Medical Center | Tech Park, Bangalore, KA\n"
    ).italic = True

    hospital_info.add_run(
        "Contact: +91 80 1234 5678 | Email: support@carepulse.ai"
    )

    doc.add_paragraph(
        "-" * 80
    ).alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Title
    sub = doc.add_heading(
        'OFFICIAL APPOINTMENT RECEIPT',
        level=1
    )

    sub.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Meta Table
    meta_table = doc.add_table(rows=1, cols=2)

    meta_table.cell(0, 0).text = (
        f"Appointment ID: CP-2024-REQ-{appt['id']}"
    )

    meta_table.cell(0, 1).text = (
        f"Date: {appt['date']}"
    )

    meta_table.cell(
        0,
        1
    ).paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT

    doc.add_paragraph()

    # Main Table
    data_table = doc.add_table(rows=0, cols=2)
    data_table.style = 'Table Grid'

    def add_row(label, value):
        row = data_table.add_row().cells

        row[0].text = label
        row[0].paragraphs[0].runs[0].bold = True

        row[1].text = str(value)

    # Patient Details
    add_row("--- PATIENT DETAILS ---", "")
    add_row("Full Name", appt['patient_name'])
    add_row("Age", f"{appt['patient_age']} Years")
    add_row("Reason for Visit", appt['issue'])

    # Consultation Details
    add_row("--- CONSULTATION DETAILS ---", "")
    add_row("Specialist Name", appt['doctor_name'])
    add_row("Specialization", appt['doctor_specialization'])
    add_row("Scheduled Slot", appt['slot'])
    add_row("Booking Status", appt['status'].upper())

    doc.add_paragraph()

    # Instructions
    instr_head = doc.add_paragraph()
    instr_head.add_run(
        "PATIENT INSTRUCTIONS:"
    ).bold = True

    instr_text = doc.add_paragraph()

    instr_text.add_run(
        "1. Please arrive at the hospital 15 minutes before your scheduled slot.\n"
    )

    instr_text.add_run(
        "2. Carry a valid ID proof and previous medical history if any.\n"
    )

    instr_text.add_run(
        "3. This receipt is valid only for the mentioned date and time."
    )

    # Footer
    footer = doc.add_paragraph("\n" * 2)
    footer.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    footer.add_run(
        "Digitally Verified by CarePulse AI\n"
    ).bold = True

    footer.add_run(
        "Authorised Clinical Portal"
    )

    disclaimer = doc.add_paragraph(
        "\nDisclaimer: This is an AI-assisted portal booking. Final diagnosis will be provided by the consultant."
    )

    disclaimer.alignment = WD_ALIGN_PARAGRAPH.CENTER

    run_d = disclaimer.runs[0]
    run_d.font.size = Pt(8)
    run_d.font.italic = True

    # Save DOCX
    target = io.BytesIO()
    doc.save(target)
    target.seek(0)

    # Download DOCX File
    return send_file(
        target,
        as_attachment=True,
        download_name=f"CarePulse_Receipt_{appt['id']}.docx",
        mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )


if __name__ == "__main__":
    app.run(debug=True)