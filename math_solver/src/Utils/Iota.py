_count: int = 0

def next() -> int:
    global _count
    _count += 1
    return _count

def reset() -> int:
    global _count
    _count = 0
    return _count

def count() -> int:
    global _count
    return _count