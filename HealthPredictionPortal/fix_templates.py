import os

index2 = r"""{% extends "base.html" %}
{% block title %}Welcome - CarePulse AI Health Portal{% endblock %}
{% block navbar %}{% endblock %}

{% block body %}
<nav class="navbar" style="position:fixed;width:100%;top:0;left:0;background:rgba(10,110,138,0.7);backdrop-filter:blur(12px);border-bottom:1px solid rgba(255,255,255,0.1);">
  <a href="/" class="navbar-brand">
    <div class="logo-icon">&#127973;</div>
    <span>Care<em>Pulse</em> AI</span>
  </a>
  <div class="nav-links">
    <a href="/login" class="btn btn-outline" style="color:white;border-color:rgba(255,255,255,0.5);padding:9px 20px;">Login</a>
    <a href="/signup" class="btn btn-success" style="padding:9px 20px;">Sign Up</a>
  </div>
</nav>

<div class="hero">
  <div class="hero-content" style="margin-top:60px;">
    <div class="hero-badge">&#9877; AI-Powered Health Intelligence</div>
    <h1>Your Health.<br><span>Predicted.</span> Protected.</h1>
    <p>Advanced AI models trained on clinical data to detect heart disease and diabetes risk instantly - right from your browser.</p>
    <div class="hero-cta">
      <a href="/signup" class="btn btn-success btn-lg">Get Started Free &rarr;</a>
      <a href="/login" class="btn btn-lg" style="background:rgba(255,255,255,0.15);color:white;backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,0.3);">Login to Portal</a>
    </div>
    <a href="tel:108" class="emergency-btn" style="font-size:1rem;padding:12px 28px;margin-bottom:48px;display:inline-flex;">&#128680; Medical Emergency? Call 108 Now</a>
    <div class="hero-stats">
      <div class="hero-stat"><div class="num">95%</div><div class="label">PREDICTION ACCURACY</div></div>
      <div class="hero-stat"><div class="num">2</div><div class="label">DISEASE MODULES</div></div>
      <div class="hero-stat"><div class="num">4+</div><div class="label">SPECIALIST DOCTORS</div></div>
      <div class="hero-stat"><div class="num">24/7</div><div class="label">EMERGENCY SUPPORT</div></div>
    </div>
  </div>
</div>

<section style="background:#f8fafc;padding:80px 20px;">
  <div style="max-width:1100px;margin:0 auto;">
    <div class="page-header">
      <span class="badge badge-primary">OUR SERVICES</span>
      <h1>Everything You Need, In One Portal</h1>
      <p>Assess risk, book specialists, and get the right care - all in minutes.</p>
    </div>
    <div class="features-grid">
      <a href="/heart" class="feature-card">
        <div class="feature-icon blue">&#10084;&#65039;</div>
        <h3>Heart Disease Analysis</h3>
        <p>AI-powered cardiac risk assessment using 13 clinical parameters. Get instant insights about your heart health.</p>
        <div class="arrow">Analyze Now &rarr;</div>
      </a>
      <a href="/diabetes" class="feature-card">
        <div class="feature-icon green">&#129504;</div>
        <h3>Diabetes Risk Check</h3>
        <p>Detect diabetes and pre-diabetes risk using blood sugar, BMI, insulin, and other key health markers.</p>
        <div class="arrow">Check Risk &rarr;</div>
      </a>
      <a href="/appointment" class="feature-card">
        <div class="feature-icon purple">&#128104;&#8205;&#9877;&#65039;</div>
        <h3>Book a Specialist</h3>
        <p>Connect with Cardiologists, Endocrinologists, and General Physicians. View slots and book instantly.</p>
        <div class="arrow">Find Doctors &rarr;</div>
      </a>
      <a href="tel:108" class="feature-card" style="border-top:4px solid #d63031;">
        <div class="feature-icon orange">&#128657;</div>
        <h3>Emergency Ambulance</h3>
        <p>One-touch call to emergency services. Available 24/7 for critical situations across India.</p>
        <div class="arrow" style="color:#d63031;">Call 108 &rarr;</div>
      </a>
    </div>
  </div>
</section>

<section style="background:linear-gradient(135deg,#0a6e8a,#053e50);padding:80px 20px;text-align:center;">
  <h2 style="color:white;font-size:2.2rem;font-weight:800;margin-bottom:16px;">Ready to Take Control of Your Health?</h2>
  <p style="color:rgba(255,255,255,0.7);font-size:1.05rem;margin-bottom:36px;">Create your free account and get your first risk assessment in under 2 minutes.</p>
  <a href="/signup" class="btn btn-success btn-lg">Create Free Account &rarr;</a>
</section>

<footer class="footer">
  <p><strong>CarePulse AI</strong> &mdash; Health Prediction Portal &copy; 2024 &nbsp;|&nbsp; &#128657; Emergency: <strong>108</strong> &nbsp;|&nbsp; Not a substitute for professional medical advice.</p>
</footer>
{% endblock %}
"""

diabetes = r"""{% extends "base.html" %}
{% block title %}Diabetes Check - CarePulse AI{% endblock %}
{% block content %}
<div class="container">
  <div class="page-header">
    <span class="badge badge-success">&#129504; ENDOCRINOLOGY</span>
    <h1>Diabetes Risk Assessment</h1>
    <p>Detect early signs of diabetes and pre-diabetes with our clinical AI model.</p>
  </div>
  <div class="info-two-col">
    <div class="card" style="border-top:4px solid #f39c12;">
      <h3 style="color:#f39c12;margin-bottom:16px;">&#9888;&#65039; Common Symptoms</h3>
      <ul class="info-list">
        <li><span class="icon">&#128992;</span>Frequent urination, especially at night</li>
        <li><span class="icon">&#128992;</span>Excessive thirst and dry mouth</li>
        <li><span class="icon">&#128992;</span>Unexplained weight loss</li>
        <li><span class="icon">&#128992;</span>Blurred vision or slow wound healing</li>
        <li><span class="icon">&#128992;</span>Constant fatigue and lack of energy</li>
        <li><span class="icon">&#128992;</span>Tingling or numbness in hands and feet</li>
      </ul>
    </div>
    <div class="card" style="border-top:4px solid #00b894;">
      <h3 style="color:#00b894;margin-bottom:16px;">&#9989; Prevention Tips</h3>
      <ul class="info-list">
        <li><span class="icon">&#128154;</span>Maintain a healthy BMI (18.5 to 24.9 range)</li>
        <li><span class="icon">&#128154;</span>Reduce refined sugar and processed carbs</li>
        <li><span class="icon">&#128154;</span>Exercise regularly - even 20 to 30 min walks help</li>
        <li><span class="icon">&#128154;</span>Monitor fasting blood glucose annually</li>
        <li><span class="icon">&#128154;</span>Eat more fiber-rich vegetables and whole grains</li>
        <li><span class="icon">&#128154;</span>Stay hydrated and limit sugary beverages</li>
      </ul>
    </div>
  </div>
  <div class="stats-row">
    <div class="stat-card"><div class="stat-num">537M</div><div class="stat-label">Adults with diabetes globally</div></div>
    <div class="stat-card"><div class="stat-num">1 in 2</div><div class="stat-label">Are undiagnosed</div></div>
    <div class="stat-card"><div class="stat-num">8</div><div class="stat-label">Parameters our AI analyzes</div></div>
    <div class="stat-card"><div class="stat-num">95%</div><div class="stat-label">Model accuracy</div></div>
  </div>
  <div class="alert-banner">&#128203; Fill in your clinical values below. Results are instant and completely confidential.</div>
  <div style="text-align:center;margin-top:8px;">
    <a href="/diabetes_form" class="btn btn-primary btn-lg">&#129514; Start Diabetes Assessment &rarr;</a>
    <a href="/appointment" class="btn btn-outline btn-lg" style="margin-left:12px;">&#128104;&#8205;&#9877;&#65039; Book Endocrinologist</a>
  </div>
</div>
{% endblock %}
"""

appointment = r"""{% extends "base.html" %}
{% block title %}Book Appointment - CarePulse AI{% endblock %}
{% block content %}
<div class="container">
  <div class="page-header">
    <span class="badge badge-primary">&#128197; APPOINTMENTS</span>
    <h1>Book a Specialist</h1>
    <p>Browse available doctors and book your consultation slot instantly.</p>
  </div>
  <div class="doctor-grid">
    <div class="doctor-card">
      <div class="doctor-avatar">&#128104;&#8205;&#9877;&#65039;</div>
      <div><h3>Dr. Rahul Sharma</h3><span class="doctor-tag">Cardiologist</span></div>
      <div class="doctor-meta"><span>&#11088; 10 Years Exp.</span><span>&#128336; 10AM - 2PM</span></div>
      <p style="font-size:0.85rem;color:#718096;">Specializes in interventional cardiology and heart failure management.</p>
      <button class="btn btn-primary btn-full" onclick="openModal('Dr. Rahul Sharma', 1)">Book Appointment</button>
    </div>
    <div class="doctor-card">
      <div class="doctor-avatar">&#128105;&#8205;&#9877;&#65039;</div>
      <div><h3>Dr. Priya Mehta</h3><span class="doctor-tag">Endocrinologist</span></div>
      <div class="doctor-meta"><span>&#11088; 8 Years Exp.</span><span>&#128336; 1PM - 5PM</span></div>
      <p style="font-size:0.85rem;color:#718096;">Expert in diabetes management, thyroid disorders and metabolic diseases.</p>
      <button class="btn btn-primary btn-full" onclick="openModal('Dr. Priya Mehta', 3)">Book Appointment</button>
    </div>
    <div class="doctor-card">
      <div class="doctor-avatar">&#128104;&#8205;&#9877;&#65039;</div>
      <div><h3>Dr. Surendra H V</h3><span class="doctor-tag">Endocrinologist</span></div>
      <div class="doctor-meta"><span>&#11088; 12 Years Exp.</span><span>&#128336; 1PM - 5PM</span></div>
      <p style="font-size:0.85rem;color:#718096;">Senior endocrinologist specializing in insulin resistance and Type 2 Diabetes.</p>
      <button class="btn btn-primary btn-full" onclick="openModal('Dr. Surendra H V', 3)">Book Appointment</button>
    </div>
    <div class="doctor-card">
      <div class="doctor-avatar">&#128105;&#8205;&#9877;&#65039;</div>
      <div><h3>Dr. Sneha Kapoor</h3><span class="doctor-tag">General Physician</span></div>
      <div class="doctor-meta"><span>&#11088; 6 Years Exp.</span><span>&#128336; 4PM - 7PM</span></div>
      <p style="font-size:0.85rem;color:#718096;">Holistic general medicine for routine checkups and chronic condition monitoring.</p>
      <button class="btn btn-primary btn-full" onclick="openModal('Dr. Sneha Kapoor', 4)">Book Appointment</button>
    </div>
  </div>
</div>

<div id="bookingModal" class="modal" onclick="if(event.target===this)closeModal()">
  <div class="modal-content">
    <button class="modal-close" onclick="closeModal()">&#10005;</button>
    <div style="margin-bottom:20px;">
      <span class="badge badge-primary">&#128197; BOOK APPOINTMENT</span>
      <h2 id="displayDoctorName" style="margin-top:8px;font-size:1.3rem;"></h2>
    </div>
    <form action="/book" method="POST">
      <input type="hidden" name="doctor_id" id="modal_doctor_id">
      <div class="input-group">
        <label>Full Name <span class="required">*</span></label>
        <input type="text" name="patient_name" placeholder="Enter your full name" required>
      </div>
      <div class="input-group">
        <label>Date of Birth <span class="required">*</span></label>
        <input type="date" id="dob" onchange="calculateAge()" required>
      </div>
      <div class="input-group">
        <label>Age (auto-calculated)</label>
        <input type="number" id="age" name="age" readonly style="background:#f1f5f9;">
      </div>
      <div class="input-group">
        <label>Select Time Slot <span class="required">*</span></label>
        <select name="slot">
          <option value="10:00 AM">10:00 AM</option>
          <option value="11:30 AM">11:30 AM</option>
          <option value="02:00 PM">02:00 PM</option>
          <option value="04:30 PM">04:30 PM</option>
        </select>
      </div>
      <div class="input-group">
        <label>Symptoms / Reason for Visit</label>
        <textarea name="issue" placeholder="Briefly describe your symptoms..."></textarea>
      </div>
      <button type="submit" class="btn btn-success btn-full">&#9989; Confirm Appointment</button>
    </form>
  </div>
</div>
{% endblock %}
{% block scripts %}
<script>
function openModal(name, id) {
  document.getElementById("displayDoctorName").innerText = "Booking with " + name;
  document.getElementById("modal_doctor_id").value = id;
  document.getElementById("bookingModal").style.display = "flex";
}
function closeModal() {
  document.getElementById("bookingModal").style.display = "none";
}
function calculateAge() {
  var dob = new Date(document.getElementById("dob").value);
  if (isNaN(dob)) return;
  document.getElementById("age").value = new Date().getFullYear() - dob.getFullYear();
}
</script>
{% endblock %}
"""

diabetes_form = r"""{% extends "base.html" %}
{% block title %}Diabetes Assessment Form - CarePulse AI{% endblock %}
{% block content %}
<div class="container">
  <div class="page-header">
    <span class="badge badge-success">&#129504; DIABETES ASSESSMENT</span>
    <h1>Diabetes Risk Form</h1>
    <p>Enter your health metrics below. The AI will analyze them instantly.</p>
  </div>
  <div class="card" style="max-width:640px;margin:0 auto;">
    <div class="steps">
      <div class="step done"><span class="step-num">&#10003;</span>Diabetes Info</div>
      <div class="step-line"></div>
      <div class="step active"><span class="step-num">2</span>Enter Details</div>
      <div class="step-line"></div>
      <div class="step"><span class="step-num">3</span>Get Results</div>
    </div>
    <form action="/predict_diabetes" method="post">
      <div class="input-group">
        <label>Pregnancies <span class="required">*</span> <small style="color:#718096">(number of times)</small></label>
        <input type="number" name="Pregnancies" placeholder="e.g. 2" min="0" required>
      </div>
      <div class="input-group">
        <label>Glucose Level <span class="required">*</span> <small style="color:#718096">(mg/dL)</small></label>
        <input type="number" name="Glucose" placeholder="e.g. 120" required>
      </div>
      <div class="input-group">
        <label>Blood Pressure <span class="required">*</span> <small style="color:#718096">(mm Hg)</small></label>
        <input type="number" name="BloodPressure" placeholder="e.g. 70" required>
      </div>
      <div class="input-group">
        <label>Skin Thickness <span class="required">*</span> <small style="color:#718096">(mm)</small></label>
        <input type="number" name="SkinThickness" placeholder="e.g. 20" required>
      </div>
      <div class="input-group">
        <label>Insulin Level <span class="required">*</span> <small style="color:#718096">(mu U/ml)</small></label>
        <input type="number" name="Insulin" placeholder="e.g. 80" required>
      </div>
      <div class="input-group">
        <label>BMI <span class="required">*</span> <small style="color:#718096">(kg/m2)</small></label>
        <input type="number" step="0.1" name="BMI" placeholder="e.g. 25.5" required>
      </div>
      <div class="input-group">
        <label>Diabetes Pedigree Function <span class="required">*</span></label>
        <input type="number" step="0.001" name="DiabetesPedigreeFunction" placeholder="e.g. 0.627" required>
      </div>
      <div class="input-group">
        <label>Age <span class="required">*</span></label>
        <input type="number" name="Age" placeholder="e.g. 35" min="1" max="120" required>
      </div>
      <div style="text-align:center;margin-top:8px;">
        <button type="submit" class="btn btn-success btn-lg" style="min-width:240px;">&#129514; Analyze Diabetes Risk &rarr;</button>
        <p style="margin-top:12px;font-size:0.82rem;color:#718096;">&#128274; Your data is processed locally and never stored.</p>
      </div>
    </form>
  </div>
</div>
{% endblock %}
"""

result = r"""{% extends "base.html" %}
{% block title %}Prediction Result - CarePulse AI{% endblock %}
{% block content %}
<div class="container">

  {% if "High Risk" in result or result == "Diabetic" %}
  <div class="result-critical">
    <div style="font-size:3rem;margin-bottom:12px;">&#128680;</div>
    <span class="badge badge-danger">CRITICAL ALERT</span>
    <h1 style="color:#d63031;font-size:2rem;margin:12px 0;">{{ result }}</h1>
    <p style="color:#7f0000;font-size:1rem;margin-bottom:28px;">Your health parameters indicate a <strong>high level of risk</strong>. Please do not delay seeking medical attention.</p>
    <a href="tel:108" class="emergency-btn" style="font-size:1.1rem;padding:16px 40px;">&#128657; Call Emergency Ambulance (108)</a>
    <p style="margin-top:16px;font-size:0.85rem;color:#718096;">Or consult the recommended specialist listed below immediately.</p>
  </div>
  {% else %}
  <div class="result-normal">
    <div style="font-size:3rem;margin-bottom:12px;">&#9989;</div>
    <span class="badge badge-success">LOW RISK</span>
    <h1 style="color:#0a6e8a;font-size:2rem;margin:12px 0;">{{ result }}</h1>
    <p style="color:#065f46;font-size:1rem;">Great news! Your current health parameters show a low risk. Keep maintaining a healthy lifestyle.</p>
  </div>
  {% endif %}

  <div style="margin:28px 0;">
    <button class="btn btn-primary" onclick="toggleHospitals()" id="hospitalBtn">&#127973; Show Recommended Hospitals</button>
  </div>

  <div id="hospitalSection" style="display:none;margin-bottom:32px;">
    <h3 style="margin-bottom:16px;">Hospitals Specializing in {{ doctor_type }} Care</h3>
    <div class="hospital-grid">
      <div class="hospital-card"><h3>&#127973; AIIMS</h3><p>New Delhi | Rating: &#11088; 4.8/5</p></div>
      <div class="hospital-card"><h3>&#127973; Apollo Hospitals</h3><p>Multi-City | Rating: &#11088; 4.7/5</p></div>
      <div class="hospital-card"><h3>&#127973; Fortis Healthcare</h3><p>Cardiac Care | Rating: &#11088; 4.6/5</p></div>
      <div class="hospital-card"><h3>&#127973; Manipal Hospitals</h3><p>Bangalore | Rating: &#11088; 4.5/5</p></div>
    </div>
  </div>

  <div class="card">
    <h3 style="margin-bottom:20px;">&#128104;&#8205;&#9877;&#65039; Available {{ doctor_type }}s - Book Now</h3>
    {% for doc in doctors %}
    <div style="border-bottom:1px solid #e2e8f0;padding:20px 0;display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:16px;">
      <div style="display:flex;align-items:center;gap:14px;">
        <div class="doctor-avatar" style="width:48px;height:48px;font-size:1.3rem;">&#128104;&#8205;&#9877;&#65039;</div>
        <div>
          <strong>{{ doc.name }}</strong>
          <p style="margin:2px 0;font-size:0.82rem;color:#718096;">{{ doc.specialization }}</p>
        </div>
      </div>
      <form action="/book" method="POST" style="display:flex;gap:10px;align-items:center;flex-wrap:wrap;">
        <input type="hidden" name="doctor_id" value="{{ doc.id }}">
        <select name="slot" style="min-width:140px;">
          {% for s in doc.slots %}<option value="{{ s }}">{{ s }}</option>{% endfor %}
        </select>
        <button type="submit" class="btn btn-success btn-sm">Book Slot</button>
      </form>
    </div>
    {% endfor %}
  </div>

  <div style="text-align:center;margin-top:16px;">
    <a href="/" class="btn btn-outline">&#127968; Back to Home</a>
  </div>
</div>
{% endblock %}
{% block scripts %}
<script>
var vis = false;
function toggleHospitals() {
  vis = !vis;
  document.getElementById("hospitalSection").style.display = vis ? "block" : "none";
  document.getElementById("hospitalBtn").textContent = vis ? "&#127973; Hide Hospitals" : "&#127973; Show Recommended Hospitals";
}
</script>
{% endblock %}
"""

files = {
    'templates/index2.html': index2,
    'templates/diabetes.html': diabetes,
    'templates/appointment.html': appointment,
    'templates/diabetes_form.html': diabetes_form,
    'templates/result.html': result,
}

for path, content in files.items():
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Written:', path)

print('All done.')
