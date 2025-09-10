#!/usr/bin/env python3
"""Simple test to check if parser_2gis can be imported and basic functionality works."""

def test_basic_import():
    """Test basic import of parser_2gis module."""
    try:
        import parser_2gis
        print("✅ parser_2gis imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Failed to import parser_2gis: {e}")
        return False

def test_models_import():
    """Test import of data models."""
    try:
        from parser_2gis.writer.models import CatalogItem
        print("✅ CatalogItem model imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Failed to import CatalogItem: {e}")
        return False

def test_pydantic_compatibility():
    """Test Pydantic model creation."""
    try:
        from parser_2gis.writer.models import CatalogItem
        
        # Create a simple CatalogItem instance
        item = CatalogItem(
            id="test_id",
            locale="ru_RU", 
            type="test"
        )
        print(f"✅ CatalogItem created successfully: {item.id}")
        return True
    except Exception as e:
        print(f"❌ Failed to create CatalogItem: {e}")
        return False

if __name__ == "__main__":
    print("Running basic compatibility tests...")
    
    tests = [
        test_basic_import,
        test_models_import, 
        test_pydantic_compatibility
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print("-" * 50)
    
    print(f"Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed!")
        exit(0)
    else:
        print("💥 Some tests failed!")
        exit(1)