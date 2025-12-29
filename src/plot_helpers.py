
def millions(x, pos):
    """The two arguments are the value and tick position."""
    return f"{x*1e-6:1.1f}M"

def thousands(x, pos):
    """The two arguments are the value and tick position."""
    return f"{x*1e-3:1.1f}k"