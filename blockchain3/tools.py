# coding:utf-8
import rsa
from dilithium_python.dilithium import Dilithium2


# def create_genisus_keypair():
#     # 第一个节点的密钥对
#     pubkey, privkey = rsa.newkeys(1024)
#     with open('genisus_public.pem', 'w+') as f:
#         f.write(pubkey.save_pkcs1().decode())
#
#     with open('genisus_private.pem', 'w+') as f:
#         f.write(privkey.save_pkcs1().decode())


def create_genisus_keypair():
    # 第一个节点的密钥对
    pubkey, privkey = Dilithium2.keygen()
    with open('genisus_public.txt', 'wb+') as f:
        f.write(pubkey)

    with open('genisus_private.txt', 'wb+') as f:
        f.write(privkey)



# # 导入密钥
# with open('genisus_private.pem', 'r') as f:
#     privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())
#
# with open('genisus_public.pem', 'r') as f:
#     pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())
#
# # 明文
# message = b'hello world'
#
# # 公钥加密
# crypto = rsa.encrypt(message.encode(), pubkey)
#
# # 私钥解密
# message = rsa.decrypt(crypto, privkey).decode()
# print(message)


# 明文
message = b'hello world'
create_genisus_keypair()
# 导入密钥
with open('genisus_private.txt', 'rb') as f:
    privkey = f.read()

with open('genisus_public.txt', 'rb') as f:
    pubkey = f.read()

# 私钥签名
print(privkey)
sig = Dilithium2.sign(privkey, message)

# 公钥验证
assert Dilithium2.verify(pubkey, message, sig)

# # 明文
# message = 'hello world'
# # 导入密钥
# with open('genisus_private.pem', 'r') as f:
#     privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())
#
# with open('genisus_public.pem', 'r') as f:
#     pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())
# # 私钥签名
# signature = rsa.sign(message.encode(), privkey, 'SHA-1')
#
# # 公钥验证
# try:
#     rsa.verify(message.encode(), signature, pubkey)
# except rsa.pkcs1.VerificationError:
#     print('invalid')
