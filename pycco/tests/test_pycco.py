from hypothesis import given
from hypothesis.strategies import lists, text, booleans
import pycco.main as p
import copy


@given(lists(text()), text())
def test_shift(fragments, default):
    if fragments == []:
        assert p.shift(fragments, default) == default
    else:
        fragments2 = copy.copy(fragments)
        head = p.shift(fragments, default)
        assert [head] + fragments == fragments2


@given(text(), booleans(), text(min_size=1))
def test_destination(filepath, preserve_paths, outdir):
    dest = p.destination(filepath, preserve_paths=preserve_paths, outdir=outdir)
    assert dest.startswith(outdir)
    assert dest.endswith(".html")
