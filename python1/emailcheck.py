import re

def is_valid_email(email: str) -> bool:
    """
    이메일 주소의 유효성을 검사합니다.

    Parameters:
    email (str): 검사할 이메일 주소

    Returns:
    bool: 유효한 이메일 주소이면 True, 그렇지 않으면 False
    """
    email_regex = re.compile(
        r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    )
    return re.match(email_regex, email) is not None

# 사용 예시
emails = ["test@example.com", "invalid-email", "another.test@domain.co", "bad@domain"]
for email in emails:
    print(f"{email}: {is_valid_email(email)}")


# 테스트 이메일 목록
emails = [
    "valid.email@example.com",
    "invalid-email",
    "another.valid.email@domain.co",
    "bad@domain",
    "valid_email123@domain.com",
    "valid.email+alias@domain.co.in",
    "invalid-email@domain..com",
    "invalid-email@-domain.com",
    "@missing-user.com"
]

# 각 이메일 주소의 유효성 검사 결과 출력
for email in emails:
    print(f"{email}: {is_valid_email(email)}")
