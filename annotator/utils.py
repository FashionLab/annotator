import base64


def load_image(name):
    ending = name.rsplit(".", 1)[-1]
    with open(name, "rb") as fp:
        return "data:image/{};base64,{}".format(
            ending, base64.b64encode(fp.read()).decode()
        )
