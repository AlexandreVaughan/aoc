
from day12 import Record,RecordSet

CONDITION_RECORD = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

def test_read_record():
    record=Record("?#?#?#?#?#?#?#? 1,3,1,6")
    assert record.damaged_record == "?#?#?#?#?#?#?#?"
    assert record.count_record == (1,3,1,6)

def test_read_recordset():
    record_set=RecordSet(CONDITION_RECORD)
    assert len(record_set.record_list) == 6
    assert record_set.record_list[0].damaged_record == "???.###"
    assert record_set.record_list[0].count_record == (1,1,3)

def test_count_arrangements():
    record=Record("???.### 1,1,3")
    assert record.count_arrangements() == 1
    record=Record(".??..??...?##. 1,1,3")
    assert record.count_arrangements() == 4
    record=Record("?#?#?#?#?#?#?#? 1,3,1,6")
    assert record.count_arrangements() == 1
    record=Record("????.#...#... 4,1,1")
    assert record.count_arrangements() == 1
    record=Record("????.######..#####. 1,6,5")
    assert record.count_arrangements() == 4
    record=Record("?###???????? 3,2,1")
    assert record.count_arrangements() == 10

def test_unfolded_arrangements():
    record=Record("???.### 1,1,3",5)
    assert record.count_arrangements() == 1
    record=Record(".??..??...?##. 1,1,3",5)
    assert record.count_arrangements() == 16384
    record=Record("?#?#?#?#?#?#?#? 1,3,1,6",5)
    assert record.count_arrangements() == 1
    record=Record("????.#...#... 4,1,1",5)
    assert record.count_arrangements() == 16
    record=Record("????.######..#####. 1,6,5",5)
    assert record.count_arrangements() == 2500
    record=Record("?###???????? 3,2,1",5)
    assert record.count_arrangements() == 506250    


