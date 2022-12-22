from day7 import *
import pytest

def test_single_elem():
    elem = FileSysElem()
    assert elem.compute_size() == 0
    elem.set_file_size(12)
    assert elem.compute_size() == 12


def test_directory_1level():
    file1 = FileSysElem()
    file1.set_file_size(12)
    file2 = FileSysElem()
    file2.set_file_size(5)
    dir = FileSysElem()
    dir.add_sub_elem("x",file1)
    dir.add_sub_elem("y",file2)
    assert dir.compute_size() == 17
    
def test_directory_2level():
    file1 = FileSysElem()
    file1.set_file_size(12)
    file2 = FileSysElem()
    file2.set_file_size(5)
    dir = FileSysElem()
    dir.add_sub_elem("x",file1)
    dir.add_sub_elem("y",file2)
    file3 = FileSysElem()
    file3.set_file_size(6)
    top_dir = FileSysElem()
    top_dir.add_sub_elem("d",dir)
    top_dir.add_sub_elem("z",file3)
    assert top_dir.compute_size() == 23

def test_retrieve_subelem():
    file1 = FileSysElem()
    file1.set_file_size(12)
    file2 = FileSysElem()
    file2.set_file_size(5)
    dir = FileSysElem()
    assert dir.retrieve_elem("toto") == None
    dir.add_sub_elem("toto",file1)
    dir.add_sub_elem("titi",file2)
    assert dir.retrieve_elem("toto").compute_size() == 12

@pytest.fixture
def test_tree():
    file1 = FileSysElem()
    file1.set_file_size(12)
    file2 = FileSysElem()
    file2.set_file_size(5)
    dir = FileSysElem()
    dir.add_sub_elem("x",file1)
    dir.add_sub_elem("y",file2)
    file3 = FileSysElem()
    file3.set_file_size(6)
    top_dir = FileSysElem()
    top_dir.add_sub_elem("d",dir)
    top_dir.add_sub_elem("z",file3)
    return top_dir


def test_cd(test_tree):
    current_dir = test_tree.cd("x")
    assert current_dir == None
    current_dir = test_tree.cd("d")
    assert current_dir.compute_size() == 17
    current_dir = current_dir.cd("x")
    assert current_dir.compute_size() == 17
    current_dir = current_dir.cd("..")
    assert current_dir.compute_size() == 23


def test_fill_ls():
    ls_result = """
    dir a
14848514 b.txt
8504156 c.dat
dir d
    """
    root = FileSysElem()
    root.fill(ls_result)
    assert root.compute_size() == 14848514+8504156
    assert root.cd("a") != None
    assert root.cd("d") != None


def test_exec_commands():
    commands = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
    """
    root_dir = FileSysElem()
    exec_commands(commands,root_dir)
    assert root_dir.compute_size() == 48381165
    dir_sizes = {}
    root_dir.get_dir_sizes(dir_sizes, "/")
    assert dir_sizes["//a/e"] == 584
    assert dir_sizes["//a"] == 94853 
    assert dir_sizes["//d"] == 24933642 
    assert root_dir.sum_sizes_at_most(100000, "/") == 95437

    assert root_dir.unused_space(70000000) == 21618835
    assert root_dir.needed_space(70000000,30000000) == 8381165
    assert root_dir.potential_free(70000000,30000000, "/") == 24933642