import uuid

def unique_name(name: str, ext: str):
    return f"{name}_{uuid.uuid4().hex}.{ext}"