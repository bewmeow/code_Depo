import json as j
from socket import *
from threading import Thread
import fileinput as f
import rich as r
import os
import logging as l
import datetime

path = r"C:\Users\tutor\PycharmProjects\CubeTron\GUI\FUNCTOOLS\CORE\baha.json"
json_dumps = j.dumps
json_dump = j.dump
json_loads = j.loads

class Json:
    _one_start = True
    _starting_text = {
    "Students": {
    },
    "Students Lenght": 0,
    "Student Order" : 0,
    "Students Short": {
    }
}
    def __init__(self, file_name):
        if self._one_start:
            f = open(file_name,"w+")
            f.write(json_dumps(self._starting_text, indent=4, sort_keys=True))
            f.close()
            self._one_start = False

        self._file_name = file_name
        self._file_text = open(file_name,"r+").read()
        self._data: object = ""
        print(self._file_text)
        self._json_text: dict = json_loads(self._file_text)
        self.Variable = self._json_text

    def writeFile(self, file_path):
        file = open(file_path, "w+")
        file.write(json_dumps(self._data, indent=4,sort_keys=True))
        file.close()

    @property
    def JsonObject(self) -> dict:
        return self._json_text

    @JsonObject.setter
    def JsonObject(self, v:object):
        self._json_text = v

    @property
    def Variable(self):
        return self._data

    @Variable.setter
    def Variable(self, v:object):
        self._data = v

    def AddStudent(self,name:str, no:int):
        self._json_text["Students"][name] = no
        self._Sort_List_Add(name, self.JsonObject["Students Lenght"])
        self.Student_Len()
        self.Update()

    def _ara(slef, keys: dict,item: int):
        for i in keys["Students"].keys():
            if keys["Students"][i] == item:
                return i
        return 0

    def DelStudent(self, name):
        self._json_text["Students"].pop(name)
        self._Sort_List_Remove(name)
        self.Student_Len()
        self.Update()

    def Student_Len(self):
        self._json_text["Students Lenght"] = len(self._json_text["Students"])
        self.Update()

    def Update(self):
        self.Variable = self._json_text
        self.writeFile(self._file_name)
        self.__init__(self._file_name)

    def _Sort_List_Add(self, name: str, i: int):
        self.JsonObject["Students Short"][name] = i

    def _Sort_List_Remove(self, name: str):
        self._json_text["Students Short"].pop(name)

    @property
    def _OrderGet(self):
        return self._json_text["Student Order"]

    @_OrderGet.setter
    def _OrderSet(self, v:int):
        self._json_text["Student Order"] = v

    def Sort_by_Students(self):
        items = []
        ndict = dict()
        for i in self._json_text["Students"].values():
            items.append(i)

        items.sort()
        print(items)
        self.Update()
        for i in items:
            name = self._ara(self._json_text,i)
            self._json_text["Students Short"][name] = items.index(i) + 1

        self.Update()

    def SortManipluation(self, isim:str, sıra:int):
        self._json_text["Students Short"][isim] = sıra
        self.Update()

    def GetOrderChoice(self):
        if self._OrderGet == self._json_text["Students Lenght"]:
            self._OrderSet = 0

        elif self._OrderGet > self._json_text["Students Lenght"]:
            self._json_text = 0

        self._OrderSet += 1
        self.Update()
