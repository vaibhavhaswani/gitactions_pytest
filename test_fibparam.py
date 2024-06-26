import pytest


@pytest.mark.parametrize('inp,out',[([1,2,3],6)])
def test_param(inp,out):
  assert sum(inp)==out