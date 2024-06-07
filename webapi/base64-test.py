import base64

# 假设这是一个 base64 编码的字符串
encoded_data = ('iVBORw0KGgoAAAANSUhEUgAAApQAAAKUAQAAAACStJWRAAAC6ElEQVR4nO3dS7LbIBCF4dOpzKUdZP'
                '7EysgAzXiJdv3Jro2qP4euPRAX7lHXSBAFnV1hF+XkxImJiYmJiYmJiYmJiYmJiYmJiYmJiYmJibm'
                'e0zFI7pbS3ktxq184qyxxzZL7piYmJiYg5q5pqSKk0qMZLbWT/aN3/Y/MTExMTFvb9oe63EhmEk6+'
                'kdVn6lrfG5eEZiYmJiY9zZ/v2qwRFlxFEwvZ4jPkjsmJiYm5oSmmZnll0iXmN8ITExMTMx7m23/qOv'
                '8hFXx+DEt8VnjPWbJHRMTExNzHLOqR8Ha27aP0uWf/dp22jjFLLljYmJiYo5jFvXovLfTvzCKjxvvMU'
                'vumJiYmJhDmmZmJgWfMme2lquOfKZddbd8tjidMHdMTExMzA+bj/tHfroP1W37aR6qi/t43bLtY3jVs'
                '7PkjomJiYk5jtnOZ/AZC32x8VJ0FstW350ld0xMTEzMccyiHnk3KJjiUZRyv8eP0jUvVKeTGmbJHRMTE'
                'xNzHPNr+9ctvmlQd5SfZf86TExMTMz/iH79UViLvlAetCuXHuWZ3zqbbjdL7piYmJiY45gP3h9JxYIj'
                'SapH6dZiqC7tJrT96P/ExMTExLy3WdWjap1r2UlSWXZyycoTHarXSLPkjomJiYk5jtnvp1r0jzZ5AUo'
                'jd16emhrVxiy5Y2JiYmKOY9rz3brLAbp8LY3N9UuPJCnMkjsmJiYm5pCmtbH67DuzPzHmy954laQlxn'
                '67hglzx8TExMT8sNm/P0rhg3FhVdqQwTf5ltQtR2J+HSYmJibmpWbzydezr5T7JnZNT+mJeUVgYmJiY'
                'mLmYTlJvsdqWvvqp4zXYWJiYmL+pOl7MYTy07D+wij3o4LVE+1ukjsmJiYm5hvNF9+HtXovBh3vj7xx'
                'WE8mfc+SOyYmJibmoGYwa6bRNV0jj6Xc7K7f+27K3DExMTExP2q+WH/0L8H6I0xMTExMTExMTExMTExM'
                'TExMTExMTExMzInNv2woHnXYh4JkAAAAAElFTkSuQmCC==')


# 解码
decoded_data = base64.b64decode(encoded_data)

# 打印解码后的数据
print(decoded_data.decode("utf-8"))