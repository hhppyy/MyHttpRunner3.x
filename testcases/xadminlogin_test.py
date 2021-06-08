# NOTE: Generated By HttpRunner v3.1.4
# FROM: testcases\xadminlogin.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseXadminlogin(HttpRunner):

    config = Config("xadmin登录").base_url("${ENV(BASE_URL)}").verify(False)

    teststeps = [
        Step(
            RunRequest("访问登录页面获取token")
            .get("/xadmin/")
            .extract()
            .with_jmespath("body", "body")
            .with_jmespath("headers.Cookie", "cookieValue")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("关联token并进行登录")
            .post("/xadmin/")
            .with_headers(
                **{
                    "Content-Type": "application/x-www-form-urlencoded",
                    "cookie": "$cookieValue",
                }
            )
            .with_data(
                {
                    "csrfmiddlewaretoken": "${re_body($body)}",
                    "username": "admin",
                    "password": "han010657",
                    "this_is_the_login_form": 1,
                    "next": "/xadmin/",
                }
            )
            # .set_allow_redirects(False)
            .extract()
            .with_jmespath("body","body1")
            .validate()

            .assert_equal("${reg_req_body($bodyvalue)}", "欢迎，admin")
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseXadminlogin().test_start()
