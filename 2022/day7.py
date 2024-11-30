class FileSysElem:
    def __init__(self) -> None:
        self._file_size = 0
        self._children = {}
        self._parent = None


    def compute_size(self):
        sum = 0
        for child in self._children.values():
            sum+=child.compute_size()
        return sum+self._file_size

    def set_file_size(self,size):
        self._file_size = size
    
    def add_sub_elem(self,name,sub_elem):
        self._children[name] = sub_elem
        sub_elem._parent = self

    def retrieve_elem(self,elem_name):
        if elem_name in self._children:
            return self._children[elem_name]
        return None

    def cd(self,dir):
        if dir == "/":
            return self
        if dir == "..":
            return self if self._parent is None else self._parent
        elem = self.retrieve_elem(dir)
        if elem is None:
            return elem
        if elem._file_size != 0:
            return self
        return elem
    
    def fill(self,ls_result):
        for line in ls_result.splitlines():
            elem_desc_list = line.split()
            if (len(elem_desc_list) != 2):
                continue
            file = FileSysElem()
            if elem_desc_list[0].isdigit():
                file.set_file_size(int(elem_desc_list[0]))
            self.add_sub_elem(elem_desc_list[1],file)

    def get_dir_sizes(self, dict_size, parent_full_name):
        for name,file in self._children.items():
            full_name = parent_full_name+"/"+name
            if file._file_size != 0:
                continue
            dict_size[full_name] = file.compute_size()
            file.get_dir_sizes(dict_size, full_name) 

    def sum_sizes_at_most(self,size_max, parent_full_name):
        sum = 0
        dir_sizes = {}
        self.get_dir_sizes(dir_sizes, parent_full_name)
        for dir_size in dir_sizes.values():
            if dir_size > size_max:
                continue
            sum+=dir_size
        return sum
    
    def unused_space(self,total_space):
        return total_space-self.compute_size()

    def needed_space(self,total_space,wanted_space):
        return wanted_space-self.unused_space(total_space)

    def potential_free(self,total_space,wanted_space, parent_full_name):
        needed_space = self.needed_space(total_space,wanted_space)
        dir_sizes = {}
        self.get_dir_sizes(dir_sizes, parent_full_name)
        dir_sizes[parent_full_name] = self.compute_size()
        potential_free = []
        for val in dir_sizes.values():
            if val >= needed_space:
                potential_free.append(val)
        return sorted(potential_free)[0]

            

def exec_commands(commands,root_dir : FileSysElem):
    current_ls_result = ""
    current_directory = root_dir
    for line in commands.splitlines():
        if line.startswith("$ ls"):
            continue
        if line.startswith("$ cd"):
            current_directory.fill(current_ls_result)
            current_ls_result = ""
            current_directory = current_directory.cd(line.replace("$ cd ", ""))
            continue
        current_ls_result += line + '\n'
    current_directory.fill(current_ls_result)
    current_ls_result = ""
            
    

with open('day7.txt') as file:
    commands = file.read()
    root_dir = FileSysElem()
    exec_commands(commands,root_dir)
    print(root_dir.sum_sizes_at_most(100000,"/"))
    print(root_dir.potential_free(70000000,30000000, "/"))

