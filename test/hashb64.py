
import hashlib
import base64

phone_number = "13888888888"

# 对手机号进行哈希操作
hashed_number = hashlib.sha256(phone_number.encode()).digest()

# 对哈希结果进行 Base64 编码
encoded_number = base64.b64encode(hashed_number).decode()

print(encoded_number)
print(len(encoded_number))
