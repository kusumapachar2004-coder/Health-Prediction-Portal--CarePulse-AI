import os

heart_form = """{% extends "base.html" %}
{% block title %}Heart Assessment Form - CarePulse AI{% endblock %}
{% block content %}
<div class="container">
  <div class="page-header">
    <span class="badge badge-danger">❤️ HEART ASSESSMENT</span>
    <h1>Heart Disease Risk Form</h1>
    <p>Enter your clinical parameters accurately for the best prediction results.</p>
  </div>

  <div class="card" style="max-width:800px;margin:0 auto;">
    <div class="steps">
      <div class="step done"><span class="step-num">✓</span>Heart Info</div>
      <div class="step-line"></div>
      <div class="step active"><span class="step-num">2</span>Enter Details</div>
      <div class="step-line"></div>
      <div class="step"><span class="step-num">3</span>Get Results</div>
    </div>

    <form action="/predict_heart" method="post">
      <div class="form-grid">
        <div class="input-group">
          <label>Age <span class="required">*</span></label>
          <input type="number" name="age" placeholder="e.g. 45" min="1" max="120" required>
        </div>
        <div class="input-group">
          <label>Sex <span class="required">*</span> <small style="color:#718096">(1=Male, 0=Female)</small></label>
          <select name="sex" required>
            <option value="">Select</option>
            <option value="1">Male (1)</option>
            <option value="0">Female (0)</option>
          </select>
        </div>
        <div class="input-group">
          <label>Chest Pain Type <span class="required">*</span> <small style="color:#718096">(0-3)</small></label>
          <select name="cp" required>
            <option value="">Select</option>
            <option value="0">0 - Typical Angina</option>
            <option value="1">1 - Atypical Angina</option>
            <option value="2">2 - Non-Anginal Pain</option>
            <option value="3">3 - Asymptomatic</option>
          </select>
        </div>
        <div class="input-group">
          <label>Resting BP <span class="required">*</span> <small style="color:#718096">(mm Hg)</small></label>
          <input type="number" name="trestbps" placeholder="e.g. 120" required>
        </div>
        <div class="input-group">
          <label>Cholesterol <span class="required">*</span> <small style="color:#718096">(mg/dl)</small></label>
          <input type="number" name="chol" placeholder="e.g. 200" required>
        </div>
        <div class="input-group">
          <label>Fasting Blood Sugar <span class="required">*</span></label>
          <select name="fbs" required>
            <option value="">Select</option>
            <option value="1">1 - Greater than 120 mg/dl</option>
            <option value="0">0 - 120 mg/dl or below</option>
          </select>
        </div>
        <div class="input-group">
          <label>Resting ECG <span class="required">*</span> <small style="color:#718096">(0-2)</small></label>
          <select name="restecg" required>
            <option value="">Select</option>
            <option value="0">0 - Normal</option>
            <option value="1">1 - ST-T Wave Abnormality</option>
            <option value="2">2 - Left Ventricular Hypertrophy</option>
          </select>
        </div>
        <div class="input-group">
          <label>Max Heart Rate <span class="required">*</span></label>
          <input type="number" name="thalach" placeholder="e.g. 150" required>
        </div>
        <div class="input-group">
          <label>Exercise Induced Angina <span class="required">*</span></label>
          <select name="exang" required>
            <option value="">Select</option>
            <option value="1">Yes (1)</option>
            <option value="0">No (0)</option>
          </select>
        </div>
        <div class="input-group">
          <label>Oldpeak (ST Depression) <span class="required">*</span></label>
          <input type="number" step="0.1" name="oldpeak" placeholder="e.g. 1.5" required>
        </div>
        <div class="input-group">
          <label>Slope of ST Segment <span class="required">*</span> <small style="color:#718096">(0-2)</small></label>
          <select name="slope" required>
            <option value="">Select</option>
            <option value="0">0 - Upsloping</option>
            <option value="1">1 - Flat</option>
            <option value="2">2 - Downsloping</option>
          </select>
        </div>
        <div class="input-group">
          <label>Major Vessels Colored <span class="required">*</span> <small style="color:#718096">(0-3)</small></label>
          <select name="ca" required>
            <option value="">Select</option>
            <option value="0">0</option><option value="1">1</option>
            <option value="2">2</option><option value="3">3</option>
          </select>
        </div>
        <div class="input-group">
          <label>Thal <span class="required">*</span> <small style="color:#718096">(1-3)</small></label>
          <select name="thal" required>
            <option value="">Select</option>
            <option value="1">1 - Normal</option>
            <option value="2">2 - Fixed Defect</option>
            <option value="3">3 - Reversible Defect</option>
          </select>
        </div>
      </div>
      <div style="margin-top:8px;text-align:center;">
        <button type="submit" class="btn btn-primary btn-lg" style="min-width:240px;">🔬 Analyze My Heart Risk &rarr;</button>
        <p style="margin-top:12px;font-size:0.82rem;color:#718096;">🔒 Your data is processed locally and never stored.</p>
      </div>
    </form>
  </div>
</div>
{% endblock %}
"""

confirmation = """{% extends "base.html" %}
{% block title %}Appointment Confirmed - CarePulse AI{% endblock %}
{% block content %}
<div class="container" style="max-width:580px;">
  <div class="card" style="text-align:center;border-top:6px solid #00b894;padding:48px 40px;">
    <div style="width:80px;height:80px;background:linear-gradient(135deg,#e6f9f4,#b2edd8);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:2.2rem;margin:0 auto 20px;">✅</div>
    <span class="badge badge-success">CONFIRMED</span>
    <h1 style="font-size:1.8rem;color:#0a6e8a;margin:16px 0 8px;">Appointment Booked!</h1>
    <p style="color:#718096;">Your consultation has been successfully scheduled. See you soon!</p>

    <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;padding:24px;text-align:left;margin:28px 0;">
      <div style="display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid #e2e8f0;">
        <span style="color:#718096;font-size:0.9rem;">Doctor</span>
        <strong>{{ doctor_name }}</strong>
      </div>
      <div style="display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid #e2e8f0;">
        <span style="color:#718096;font-size:0.9rem;">Time Slot</span>
        <strong>{{ slot }}</strong>
      </div>
      <div style="display:flex;justify-content:space-between;padding:10px 0;">
        <span style="color:#718096;font-size:0.9rem;">Status</span>
        <strong style="color:#00b894;">✅ Confirmed</strong>
      </div>
    </div>

    <div style="display:flex;flex-direction:column;gap:12px;">
      <a href="/download_receipt" class="btn btn-primary">📄 Download Receipt</a>
      <a href="/" class="btn btn-outline">🏠 Back to Home</a>
    </div>
  </div>
</div>
{% endblock %}
"""

already_booked = """{% extends "base.html" %}
{% block title %}Already Booked - CarePulse AI{% endblock %}
{% block content %}
<div class="container" style="max-width:560px;">
  <div class="card" style="text-align:center;border-top:6px solid #f39c12;padding:48px 40px;">
    <div style="width:80px;height:80px;background:linear-gradient(135deg,#fff4e6,#fdd3a0);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:2.2rem;margin:0 auto 20px;">⚠️</div>
    <span class="badge" style="background:#fff4e6;color:#92400e;">DUPLICATE BOOKING</span>
    <h1 style="font-size:1.8rem;color:#f39c12;margin:16px 0 8px;">Already Booked</h1>
    <p style="color:#718096;">You already have an active appointment scheduled. Only one booking is allowed at a time.</p>

    <div style="background:#fff9f0;border:1px solid #fde68a;border-radius:12px;padding:24px;text-align:left;margin:28px 0;">
      <div style="display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid #fde68a;">
        <span style="color:#718096;font-size:0.9rem;">Scheduled With</span>
        <strong>{{ doctor_name }}</strong>
      </div>
      <div style="display:flex;justify-content:space-between;padding:10px 0;">
        <span style="color:#718096;font-size:0.9rem;">Time Slot</span>
        <strong>{{ slot }}</strong>
      </div>
    </div>

    <div style="display:flex;flex-direction:column;gap:12px;">
      <a href="/download_receipt" class="btn btn-danger">📄 Download Your Receipt</a>
      <a href="/" class="btn btn-outline">🏠 Back to Home</a>
    </div>
  </div>
</div>
{% endblock %}
"""

files = {
    'templates/heart_form.html': heart_form,
    'templates/confirmation.html': confirmation,
    'templates/already_booked.html': already_booked,
}
for path, content in files.items():
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Written:', path)

print('Done.')
