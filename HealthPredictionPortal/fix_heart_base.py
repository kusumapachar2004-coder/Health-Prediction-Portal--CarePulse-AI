heart_html = """{% extends "base.html" %}
{% block title %}Heart Health - CarePulse AI{% endblock %}
{% block content %}
<div class="container">
  <div class="page-header">
    <span class="badge badge-danger">❤️ CARDIOLOGY</span>
    <h1>Heart Health Hub</h1>
    <p>Understand your cardiac health risk with our AI-powered assessment tool.</p>
  </div>

  <div class="info-two-col">
    <div class="card" style="border-top:4px solid #d63031;">
      <h3 style="color:#d63031;margin-bottom:16px;">⚠️ Common Symptoms</h3>
      <ul class="info-list">
        <li><span class="icon">🔴</span>Chest pain, pressure, or tightness (Angina)</li>
        <li><span class="icon">🔴</span>Shortness of breath during activity or at rest</li>
        <li><span class="icon">🔴</span>Pain radiating to neck, jaw, shoulder, or arm</li>
        <li><span class="icon">🔴</span>Irregular heartbeat or palpitations</li>
        <li><span class="icon">🔴</span>Dizziness, lightheadedness, or fainting</li>
        <li><span class="icon">🔴</span>Unusual fatigue, especially in women</li>
      </ul>
    </div>
    <div class="card" style="border-top:4px solid #00b894;">
      <h3 style="color:#00b894;margin-bottom:16px;">✅ Prevention Tips</h3>
      <ul class="info-list">
        <li><span class="icon">💚</span>Exercise at least 30 minutes, 5 days a week</li>
        <li><span class="icon">💚</span>Maintain a heart-healthy, low-sodium diet</li>
        <li><span class="icon">💚</span>Monitor blood pressure regularly (target: &lt;120/80)</li>
        <li><span class="icon">💚</span>Avoid smoking and limit alcohol consumption</li>
        <li><span class="icon">💚</span>Manage stress through yoga, meditation, or hobbies</li>
        <li><span class="icon">💚</span>Get regular cholesterol and blood sugar checks</li>
      </ul>
    </div>
  </div>

  <div class="stats-row">
    <div class="stat-card"><div class="stat-num">17.9M</div><div class="stat-label">Deaths globally per year</div></div>
    <div class="stat-card"><div class="stat-num">80%</div><div class="stat-label">Cases are preventable</div></div>
    <div class="stat-card"><div class="stat-num">13</div><div class="stat-label">Parameters our AI analyzes</div></div>
    <div class="stat-card"><div class="stat-num">95%</div><div class="stat-label">Model accuracy</div></div>
  </div>

  <div class="alert-banner">
    📋 Our AI has been trained on clinical datasets. Enter your details below for an instant, confidential risk assessment.
  </div>

  <div style="text-align:center;margin-top:8px;">
    <a href="/heart_form" class="btn btn-primary btn-lg">🔬 Start Heart Assessment &rarr;</a>
    <a href="/appointment" class="btn btn-outline btn-lg" style="margin-left:12px;">👨‍⚕️ Book Cardiologist</a>
  </div>
</div>
{% endblock %}
"""

base_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Health Prediction Portal - AI-driven risk assessment and instant doctor consultations">
  <title>{% block title %}Health Prediction Portal{% endblock %}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
  {% block head %}{% endblock %}
</head>
<body>

{% block navbar %}
<nav class="navbar">
  <a href="/" class="navbar-brand">
    <div class="logo-icon">🏥</div>
    <span>Care<em>Pulse</em> AI</span>
  </a>
  <div class="nav-links">
    <a href="/" {% if request.path == '/' %}class="active"{% endif %}>Home</a>
    <a href="/heart" {% if request.path == '/heart' %}class="active"{% endif %}>❤️ Heart</a>
    <a href="/diabetes" {% if request.path == '/diabetes' %}class="active"{% endif %}>🩸 Diabetes</a>
    <a href="/appointment" {% if request.path == '/appointment' %}class="active"{% endif %}>📅 Appointment</a>
    <a href="tel:108" class="emergency-btn">🚑 Call 108</a>
  </div>
</nav>
{% endblock %}

{% block body %}
<main>
  {% block content %}{% endblock %}
</main>
{% endblock %}

<footer class="footer">
  <p><strong>CarePulse AI</strong> &mdash; Health Prediction Portal &copy; 2024 &nbsp;|&nbsp; 🚑 Emergency: <strong>108</strong> &nbsp;|&nbsp; Not a substitute for professional medical advice.</p>
</footer>

{% block scripts %}{% endblock %}
</body>
</html>
"""

with open('templates/heart.html', 'w', encoding='utf-8') as f:
    f.write(heart_html)
print('heart.html OK')

with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.write(base_html)
print('base.html OK')
