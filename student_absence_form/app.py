from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)

# Cấu hình Flask-Mail với Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'  # Thay bằng email của bạn
app.config['MAIL_PASSWORD'] = 'your_password'         # Thay bằng mật khẩu của bạn hoặc App Password nếu dùng Gmail

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        student_name = request.form['student_name']
        subject = request.form['subject']
        reason = request.form['reason']

        # Tạo và gửi email
        msg = Message(
            subject="Đơn xin nghỉ học",
            sender=app.config['MAIL_USERNAME'],
            recipients=['your_email@gmail.com'],  # Email nhận thông báo
            body=f"Tên học sinh: {student_name}\nMôn: {subject}\nLý do xin nghỉ: {reason}"
        )
        mail.send(msg)

        return "Đơn xin nghỉ học đã được gửi!"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
