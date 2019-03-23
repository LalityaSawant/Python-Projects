from pathlib import Path

# Absoulte Path
# c:\Program Files\microsoft
# Relative Path

path = Path("ecommerce")
print(f'ecommerce {path.exists()}')

path = Path("emails")
print(f'emails {path.exists()}')
print(path.rmdir())
print(f'emails {path.exists()}')
print(path.mkdir())
print(f'emails {path.exists()}')
print(path.rmdir())
print(f'emails {path.exists()}')
