from flask import Flask, Blueprint
from controller.users import Users
#controller에서 전달받은 데이터를 브라우저에 보여주기 위함?

user = Blueprint('user', __name__)

# 복잡한 소스파일에서는 코드를 분리하여 MVC 패턴을 정확하게 따라서,
# 리턴할 view 데이터 생성을 위한 함수들을 control 에 넣을 수 있음
# 간단한 코드일 경우에는, 기능별로 모아놓는 것이 여러 파일을 왔디갔다하지 않아서, 더 유용함
# MVC 패턴은 케이스에 따라 사용하는 것이 합리적임
@blog_abtest.route('/auth')
@login_required
def auth_test():
    return 'auth'

@user.route('/set_email')
def set_email():
    user_email = request.args.get('user_email')
    blog_id = request.args.get('blog_id')
    user = Users.create(user_email, blog_id)
    login_user(user, remember=True, duration=datetime.timedelta(days=365))

    # return render_template(get_blog_page(blog_id), user_email=user_email)
    # return redirect(url_for('blog.blog', blog_id=blog_id, user_email=user_email))
    return redirect(url_for('blog.blog'))

