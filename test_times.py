from times import time_range, compute_overlap_time

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    
    result = compute_overlap_time(large, short)
    expected = [
        ('2010-01-12 10:30:00', '2010-01-12 10:37:00'),
        ('2010-01-12 10:38:00', '2010-01-12 10:45:00')
    ]
    assert result == expected

def test_no_overlap():
    r1 = time_range("2020-01-01 10:00:00", "2020-01-01 11:00:00")
    r2 = time_range("2020-01-01 12:00:00", "2020-01-01 13:00:00")

    result = compute_overlap_time(r1, r2)
    expected = [] 
    assert result == expected


def test_multiple_intervals_each():
    r1 = time_range("2020-01-01 10:00:00", "2020-01-01 11:00:00", 2, 60)
    r2 = time_range("2020-01-01 10:30:00", "2020-01-01 11:30:00", 2, 60)

    result = compute_overlap_time(r1, r2)
    assert all(isinstance(t[0], str) and isinstance(t[1], str) for t in result)
    assert len(result) > 0


def test_touching_ranges():
    r1 = time_range("2020-01-01 10:00:00", "2020-01-01 11:00:00")
    r2 = time_range("2020-01-01 11:00:00", "2020-01-01 12:00:00")

    result = compute_overlap_time(r1, r2)
    expected = [] 
    assert result == expected
