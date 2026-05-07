login_html = r"""{% extends "base.html" %}
{% block title %}Login - CarePulse AI{% endblock %}
{% block navbar %}{% endblock %}
{% block body %}
<div class="auth-page">
  <div class="auth-card">
    <div class="logo">
      <div style="font-size:2.8rem;margin-bottom:8px;">&#127973;</div>
      <h2>Welcome Back</h2>
      <p>Login to your CarePulse AI account</p>
    </div>
    <form id="loginForm" onsubmit="return handleLogin(event)">
      <div class="input-group">
        <label for="username">Username <span class="required">*</span></label>
        <input type="text" id="username" name="username" placeholder="Enter your username" autocomplete="username">
      </div>
      <div class="input-group">
        <label for="password">Password <span class="required">*</span></label>
        <input type="password" id="password" name="password" placeholder="Enter your password" autocomplete="current-password">
      </div>
      <button type="submit" class="btn btn-primary btn-full btn-lg" id="loginBtn">Login to Portal</button>
    </form>
    <div class="divider">or</div>
    <div class="auth-footer">Don't have an account? <a href="/signup">Sign up free</a></div>
    <div class="auth-footer" style="margin-top:12px;"><a href="/">&larr; Back to Home</a></div>
  </div>
</div>

<div id="popup" class="popup">
  <div class="popup-content">
    <div id="popupIcon" style="font-size:2.5rem;margin-bottom:10px;">&#9989;</div>
    <h3 id="popupTitle">Success</h3>
    <p id="popup-message" style="margin:10px 0 20px;"></p>
    <button class="btn btn-primary" onclick="closePopup()">OK</button>
  </div>
</div>
{% endblock %}
{% block scripts %}
<script>
function handleLogin(e) {
  e.preventDefault();
  var user = document.getElementById("username").value.trim();
  var pass = document.getElementById("password").value.trim();
  var btn = document.getElementById("loginBtn");
  if (!user || !pass) { showPopup("Missing Fields","Please enter both username and password.",false); return false; }
  btn.textContent = "Logging in..."; btn.disabled = true;
  setTimeout(function() {
    showPopup("Login Successful!","Welcome back to CarePulse AI. Redirecting...",true);
    setTimeout(function() { window.location.href = "/"; }, 1500);
  }, 800);
  return false;
}
function showPopup(title, msg, ok) {
  document.getElementById("popupIcon").innerHTML = ok ? "&#9989;" : "&#9888;&#65039;";
  document.getElementById("popupTitle").textContent = title;
  document.getElementById("popup-message").textContent = msg;
  document.getElementById("popup").style.display = "flex";
}
function closePopup() { document.getElementById("popup").style.display = "none"; }
</script>
{% endblock %}
"""

signup_html = r"""{% extends "base.html" %}
{% block title %}Sign Up - CarePulse AI{% endblock %}
{% block navbar %}{% endblock %}
{% block body %}
<div class="auth-page">
  <div class="auth-card">
    <div class="logo">
      <div style="font-size:2.8rem;margin-bottom:8px;">&#9877;&#65039;</div>
      <h2>Create Account</h2>
      <p>Join CarePulse AI for free health assessments</p>
    </div>
    <form id="signupForm" onsubmit="return handleSignup(event)">
      <div class="input-group">
        <label for="fullname">Full Name <span class="required">*</span></label>
        <input type="text" id="fullname" placeholder="Enter your full name" autocomplete="name">
      </div>
      <div class="input-group">
        <label for="newuser">Username <span class="required">*</span></label>
        <input type="text" id="newuser" placeholder="Choose a username" autocomplete="username">
      </div>
      <div class="input-group">
        <label for="email">Email Address <span class="required">*</span></label>
        <input type="email" id="email" placeholder="Enter your email" autocomplete="email">
      </div>
      <div class="input-group">
        <label for="newpass">Password <span class="required">*</span></label>
        <input type="password" id="newpass" placeholder="Create a strong password" autocomplete="new-password">
      </div>
      <button type="submit" class="btn btn-success btn-full btn-lg" id="signupBtn">Create My Account</button>
    </form>
    <div class="divider">or</div>
    <div class="auth-footer">Already have an account? <a href="/login">Login here</a></div>
    <div class="auth-footer" style="margin-top:12px;"><a href="/">&larr; Back to Home</a></div>
  </div>
</div>

<div id="popup" class="popup">
  <div class="popup-content">
    <div id="popupIcon" style="font-size:2.5rem;margin-bottom:10px;">&#9989;</div>
    <h3 id="popupTitle">Success</h3>
    <p id="popup-message" style="margin:10px 0 20px;"></p>
    <button class="btn btn-primary" onclick="closePopup()">OK</button>
  </div>
</div>
{% endblock %}
{% block scripts %}
<script>
function handleSignup(e) {
  e.preventDefault();
  var name = document.getElementById("fullname").value.trim();
  var user = document.getElementById("newuser").value.trim();
  var email = document.getElementById("email").value.trim();
  var pass = document.getElementById("newpass").value.trim();
  var btn = document.getElementById("signupBtn");
  if (!name||!user||!email||!pass) { showPopup("Missing Fields","Please fill in all required fields.",false); return false; }
  if (!email.includes("@")) { showPopup("Invalid Email","Please enter a valid email address.",false); return false; }
  if (pass.length < 6) { showPopup("Weak Password","Password must be at least 6 characters.",false); return false; }
  btn.textContent = "Creating account..."; btn.disabled = true;
  setTimeout(function() {
    showPopup("Account Created!","Welcome to CarePulse AI! Redirecting to login...",true);
    setTimeout(function() { window.location.href = "/login"; }, 1800);
  }, 900);
  return false;
}
function showPopup(title, msg, ok) {
  document.getElementById("popupIcon").innerHTML = ok ? "&#127881;" : "&#9888;&#65039;";
  document.getElementById("popupTitle").textContent = title;
  document.getElementById("popup-message").textContent = msg;
  document.getElementById("popup").style.display = "flex";
}
function closePopup() { document.getElementById("popup").style.display = "none"; }
</script>
{% endblock %}
"""

with open('templates/login.html', 'w', encoding='utf-8') as f:
    f.write(login_html)
print('login.html OK')

with open('templates/signup.html', 'w', encoding='utf-8') as f:
    f.write(signup_html)
print('signup.html OK')
