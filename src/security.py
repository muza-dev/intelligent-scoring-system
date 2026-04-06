import hashlib
import os

def hash_password(password: str) -> str:
    """Hash a password for storing."""
    # Create a random salt
    salt = os.urandom(32)
    
    # Hash the password using the salt
    # We use pbkdf2 with sha256
    pwd_hash = hashlib.pbkdf2_hmac(
        'sha256', 
        password.encode('utf-8'), 
        salt, 
        100000
    )
    
    # Store the salt alongside the hash, separated by a colon
    return salt.hex() + ':' + pwd_hash.hex()

def verify_password(stored_password: str, provided_password: str) -> bool:
    """Verify a stored password against one provided by user."""
    # Split the stored password into salt and hash
    try:
        salt_hex, hash_hex = stored_password.split(':')
        salt = bytes.fromhex(salt_hex)
        stored_hash = bytes.fromhex(hash_hex)
        
        # Hash the provided password with the stored salt
        pwdhash = hashlib.pbkdf2_hmac(
            'sha256', 
            provided_password.encode('utf-8'), 
            salt, 
            100000
        )
        
        # Compare the hashes safely
        return pwdhash == stored_hash
    except Exception:
        return False
