def reverse(ss):
    if len(ss)<1:
        return ""
    else:
        return ss[-1] + reverse(ss[:-1])

print("string", reverse("string"))
