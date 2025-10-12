#!/usr/bin/env python3
"""Test script to verify the bot structure and dependencies."""

import sys
import importlib.util

def test_import(module_name, file_path=None):
    """Test if a module can be imported."""
    try:
        if file_path:
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        else:
            __import__(module_name)
        print(f"✅ {module_name} - OK")
        return True
    except ImportError as e:
        print(f"❌ {module_name} - Import Error: {e}")
        return False
    except Exception as e:
        print(f"⚠️  {module_name} - Other Error: {e}")
        return False

def main():
    """Run structure tests."""
    print("🧪 Testing Portuguese Helper Bot Structure...\n")
    
    print("📦 Testing Python dependencies:")
    dependencies = [
        "telegram",
        "openai", 
        "dotenv",
        "requests",
        "re",
        "os",
        "logging",
        "asyncio"
    ]
    
    dep_results = []
    for dep in dependencies:
        dep_results.append(test_import(dep))
    
    print("\n🔧 Testing bot modules:")
    module_results = []
    
    # Test if config can be loaded (without actual env vars)
    try:
        # Create dummy env vars for testing
        import os
        os.environ['TELEGRAM_BOT_TOKEN'] = 'test_token'
        os.environ['OPENAI_API_KEY'] = 'test_key'
        
        module_results.append(test_import("config", "config.py"))
        module_results.append(test_import("openai_helper", "openai_helper.py"))
        module_results.append(test_import("bot", "bot.py"))
        
        # Clean up test env vars
        del os.environ['TELEGRAM_BOT_TOKEN']
        del os.environ['OPENAI_API_KEY']
        
    except Exception as e:
        print(f"❌ Module testing failed: {e}")
        module_results = [False, False, False]
    
    print("\n📊 Results:")
    print(f"Dependencies: {sum(dep_results)}/{len(dep_results)} OK")
    print(f"Bot Modules: {sum(module_results)}/{len(module_results)} OK")
    
    if all(dep_results) and all(module_results):
        print("\n🎉 All tests passed! Bot structure is ready.")
        print("\n📋 Next steps:")
        print("1. Copy .env.example to .env")
        print("2. Add your TELEGRAM_BOT_TOKEN and OPENAI_API_KEY to .env")
        print("3. Run: python bot.py")
        return True
    else:
        print("\n❌ Some tests failed. Please check the errors above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)