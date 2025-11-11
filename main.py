def make_set(capacity: int):
    """Create a hash set with given number of buckets."""
    return {
        "buckets": [[] for _ in range(capacity)],
        "count": 0
    }


def _bucket_index(s, key):
    """Compute index for the given key."""
    return hash(key) % len(s["buckets"])


def add(s, key):
    """Add key to set if not present. Return True if added, False if already exists."""
    idx = _bucket_index(s, key)
    bucket = s["buckets"][idx]

    # Check if already exists
    for k in bucket:
        if k == key:
            return False

    # Insert
    bucket.append(key)
    s["count"] += 1
    return True


def contains(s, key):
    """Return True if key exists in the set."""
    idx = _bucket_index(s, key)
    bucket = s["buckets"][idx]
    for k in bucket:
        if k == key:
            return True
    return False


def remove(s, key):
    """Remove key if present. Return True if removed, False if not found."""
    idx = _bucket_index(s, key)
    bucket = s["buckets"][idx]

    for i, k in enumerate(bucket):
        if k == key:
            del bucket[i]
            s["count"] -= 1
            return True

    return False


def size(s):
    """Return number of elements in the set."""
    return s["count"]
