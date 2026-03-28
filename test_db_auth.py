import sys
import os

# Add the project root to the path so we can import src modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.db import init_db, add_user, get_user_hash
from src.security import hash_password, verify_password
import sqlite3

def run_tests():
    print("Running DB Integration Tests...")
    
    # 1. Initialize the DB
    print("1. Initializing database...")
    init_db()
    
    # Check if table exists
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    if not c.fetchone():
        print("FAILED: Table 'users' does not exist.")
        return False
    print("SUCCESS: Table 'users' created.")
    
    # 2. Test Password Hashing
    print("\n2. Testing password hashing...")
    test_password = "my_secure_password"
    hashed = hash_password(test_password)
    
    if verify_password(hashed, test_password):
        print("SUCCESS: Password hashed and verified correctly.")
    else:
        print("FAILED: Password verification failed.")
        return False
        
    if verify_password(hashed, "wrong_password"):
        print("FAILED: Password verification succeeded with wrong password.")
        return False
    print("SUCCESS: Password rejected incorrect attempt.")

    # 3. Test Add User
    print("\n3. Testing adding a user to DB...")
    # Clean up test user if it exists from a previous run
    c.execute("DELETE FROM users WHERE username='test_user_123'")
    conn.commit()
    
    success = add_user("test_user_123", hashed)
    if success:
        print("SUCCESS: Added user 'test_user_123'.")
    else:
        print("FAILED: Could not add user 'test_user_123'.")
        return False
        
    # Test Duplicate User
    success2 = add_user("test_user_123", hashed)
    if not success2:
        print("SUCCESS: Duplicate user rejected correctly.")
    else:
        print("FAILED: Allowed duplicate user insertion.")
        return False

    # 4. Test Retrieve and Verify User
    print("\n4. Testing retrieving and verifying from DB...")
    stored_hash = get_user_hash("test_user_123")
    if stored_hash and verify_password(stored_hash, test_password):
        print("SUCCESS: Retrieved hash from DB and verified correctly.")
    else:
        print("FAILED: Could not retrieve or verify hash from DB.")
        return False

    print("\nAll DB Auth tests passed!")
    
    # Cleanup
    c.execute("DELETE FROM users WHERE username='test_user_123'")
    conn.commit()
    conn.close()
    return True

if __name__ == "__main__":
    run_tests()
