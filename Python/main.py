from src import nexon
try:
    from src import secret
except:
    from src import secretGitHub as secret

# a
if secret.Key == "":
    api = nexon.api.maplestorym.mapleMapi(secret.TestKey)
else:
    api = nexon.api.maplestorym.mapleMapi(secret.Key)

# do some code below
