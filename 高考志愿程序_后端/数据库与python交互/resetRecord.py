from DB_handler import DB_handler
from DB_methods import DB_methods

class resetRecords():
    def __init__(self, user_ID):
        self.DBh = DB_handler()
        self.DBm = DB_methods()
        self.user = user_ID
        store = self.DBh.select(['client'], ['score','province','subject','year','pici','choose_list'], ['user_ID =' + user_ID])
        self.score = str(store[0])
        self.provinceID = str(store[1])
        #print(self.provinceID)
        self.subject = store[2]
        self.year = str(store[3])
        self.pici = str(store[4])
        self.intension_list = []
        self.mid_list = store[5][:-1].split(',')
        #print(self.mid_list)
        for element in self.mid_list:
            self.intension_list.append(element[:-1].split('.'))
        #print(self.intension_list)
        self.intension_list_new = []
        self.mid_list_new = store[5][:-1].split(',') #可能会有改动client换成记录表名字
        for element in self.mid_list_new:
            self.intension_list_new.append(element[:-1].split('.'))


    def remove(self):
        school_list = []
        for i in range(len(self.intension_list)):
            school_list.append(self.intension_list[i][0])
        for j in range(len(school_list)):
            school_str = str(school_list[j])

            serial = str(j+1)
            Conditionlist = ['schoolID =' + school_str, 'provinceID =' + self.provinceID,
                             'subject ='  + self.subject , 'pici =' + self.pici,'serialnumber ='+serial]

            #先对学校进行改信息
            if int(self.score) < 430 :
                store_pre = self.DBh.select(['intension_school_table'], ['block1'], Conditionlist)
                if store_pre == None or store_pre == '':
                    print("value null")
                    break
                else:
                    store = store_pre.split(',')[1][:-1].split('.') #记录的列表
                    count = store_pre.split(',')[0] #记录人数

                    if int(count) == 1:
                        result_str = ''
                    else:
                        store.remove(self.score)
                        count = str(int(count)-1)
                        result_str = count+','
                        for element in store:
                            result_str = result_str + element +'.'
                    self.DBh.update('intension_school_table',['block1 ='+result_str],Conditionlist)

            elif int(self.score) < 510 :
                store_pre = self.DBh.select(['intension_school_table'], ['block2'], Conditionlist)
                if store_pre == None or store_pre == '':
                    print("value null")
                    break
                else:
                    store = store_pre.split(',')[1][:-1].split('.')  # 记录的列表
                    count = store_pre.split(',')[0]  # 记录人数

                    if int(count) == 1:
                        result_str = ''
                    else:
                        store.remove(self.score)
                        count = str(int(count) - 1)
                        result_str = count + ','
                        for element in store:
                            result_str = result_str + element + '.'
                    self.DBh.update('intension_school_table', ['block2 =' + '\"' + result_str + '\"'], Conditionlist)

            elif int(self.score) < 590 :
                store_pre = self.DBh.select(['intension_school_table'], ['block3'], Conditionlist)
                if store_pre == None or store_pre == '':
                    print("value null")
                    break
                else:
                    store = store_pre.split(',')[1][:-1].split('.')  # 记录的列表
                    count = store_pre.split(',')[0]  # 记录人数

                    if int(count) == 1:
                        result_str = ''
                    else:
                        store.remove(self.score)
                        count = str(int(count) - 1)
                        result_str = count + ','
                        for element in store:
                            result_str = result_str + element + '.'
                    self.DBh.update('intension_school_table', ['block3 =' + '\"' + result_str + '\"'], Conditionlist)

            elif int(self.score) < 670 :
                store_pre = self.DBh.select(['intension_school_table'], ['block4'], Conditionlist)
                if store_pre == None or store_pre == '':
                    print("value null")
                    break
                else:
                    store = store_pre.split(',')[1][:-1].split('.')  # 记录的列表
                    count = store_pre.split(',')[0]  # 记录人数

                    if int(count) == 1:
                        result_str = ''
                    else:
                        store.remove(self.score)
                        count = str(int(count) - 1)
                        result_str = count + ','
                        for element in store:
                            result_str = result_str + element + '.'
                    self.DBh.update('intension_school_table', ['block4 =' + '\"' + result_str + '\"'], Conditionlist)

            elif int(self.score) < 750 :
                store_pre = self.DBh.select(['intension_school_table'], ['block5'], Conditionlist)
                if store_pre == None or store_pre == '':
                    print("value null")
                    break
                else:
                    store = store_pre.split(',')[1][:-1].split('.')  # 记录的列表
                    count = store_pre.split(',')[0]  # 记录人数

                    if int(count) == 1:
                        result_str = ''
                    else:
                        store.remove(self.score)
                        count = str(int(count) - 1)
                        result_str = count + ','
                        for element in store:
                            result_str = result_str + element + '.'
                    self.DBh.update('intension_school_table', ['block5 =' + '\"' + result_str + '\"'], Conditionlist)



            #对每个学校的每个专业进行修改：
            zhuanye_list = []
            for k in range(len(self.intension_list[j])-1):
                k1 = k+1
                zhuanye_list.append(self.intension_list[j][k1]) #记录某学校的专业选择情况
            for l in range(len(zhuanye_list)):#对每个专业
                serial = str(l+1)
                zhuanye_str = zhuanye_list[l]
                Conditionlist = ['schoolID =' + school_str, 'provinceID =' + self.provinceID,
                                 'subject ='  + self.subject , 'pici =' + self.pici,
                                 'zhuanye='+zhuanye_str,#可能是str，要修改
                                 'serialnumber =' + serial]

                if int(self.score) < 430:
                    store_pre = self.DBh.select(['intension_zhuanye_table'], ['block1'], Conditionlist)
                    if store_pre == None or store_pre == '':
                        print("value null")
                        break
                    else:
                        store = store_pre.split(',')[1][:-1].split('.')  # 记录的列表
                        count = store_pre.split(',')[0]  # 记录人数

                        if int(count) == 1:
                            result_str = ''
                        else:
                            store.remove(self.score)
                            count = str(int(count) - 1)
                            result_str = sount + ','
                            for element in store:
                                result_str = result_str + element + '.'

                elif int(self.score) < 510:
                    store_pre = self.DBh.select(['intension_zhuanye_table'], ['block2'], Conditionlist)
                    if store_pre == None or store_pre == '':
                        print("value null")
                        break
                    else:
                        store = store_pre.split(',')[1][:-1].split('.')  # 记录的列表
                        count = store_pre.split(',')[0]  # 记录人数

                        if int(count) == 1:
                            result_str = ''
                        else:
                            store.remove(self.score)
                            count = str(int(count) - 1)
                            result_str = sount + ','
                            for element in store:
                                result_str = result_str + element + '.'
                        self.DBh.update('intension_zhuanye_table', ['block1 =' + '\"' + result_str + '\"'],
                                        Conditionlist)

                elif int(self.score) < 590:
                    store_pre = self.DBh.select(['intension_zhuanye_table'], ['block3'], Conditionlist)
                    if store_pre == None or store_pre == '':
                        print("value null")
                        break
                    else:
                        store = store_pre.split(',')[1][:-1].split('.')  # 记录的列表
                        count = store_pre.split(',')[0]  # 记录人数

                        if int(count) == 1:
                            result_str = ''
                        else:
                            store.remove(self.score)
                            count = str(int(count) - 1)
                            result_str = sount + ','
                            for element in store:
                                result_str = result_str + element + '.'
                        self.DBh.update('intension_zhuanye_table', ['block3 =' + '\"' + result_str + '\"'],
                                        Conditionlist)

                elif int(self.score) < 670:
                    store_pre = self.DBh.select(['intension_zhuanye_table'], ['block4'], Conditionlist)
                    if store_pre == None or store_pre == '':
                        print("value null")
                        break
                    else:
                        store = store_pre.split(',')[1][:-1].split('.')  # 记录的列表
                        count = store_pre.split(',')[0]  # 记录人数

                        if int(count) == 1:
                            result_str = ''
                        else:
                            store.remove(self.score)
                            count = str(int(count) - 1)
                            result_str = sount + ','
                            for element in store:
                                result_str = result_str + element + '.'
                        self.DBh.update('intension_zhuanye_table', ['block4 =' + '\"' + result_str + '\"'],
                                        Conditionlist)

                elif int(self.score) < 750:
                    store_pre = self.DBh.select(['intension_zhuanye_table'], ['block5'], Conditionlist)
                    if store_pre == None or store_pre == '':
                        print("value null")
                        break
                    else:
                        store = store_pre.split(',')[1][:-1].split('.')  # 记录的列表
                        count = store_pre.split(',')[0]  # 记录人数

                        if int(count) == 1:
                            result_str = ''
                        else:
                            store.remove(self.score)
                            count = str(int(count) - 1)
                            result_str = sount + ','
                            for element in store:
                                result_str = result_str + element + '.'
                        self.DBh.update('intension_zhuanye_table', ['block5 =' + '\"' + result_str + '\"'],
                                        Conditionlist)

    def update(self):
        school_list = []
        for i in range(len(self.intension_list)):
            school_list.append(self.intension_list[i][0])
        for j in range(len(school_list)):
            school_str = str(school_list[j])
            #print(school_list)
            serial = str(j + 1)
            Conditionlist = ['schoolID =' + school_str, 'provinceID =' + self.provinceID,
                             'subject ='  + self.subject , 'pici =' + self.pici, 'serialnumber =' + serial]

            # 先对学校进行改信息
            if int(self.score) < 430:
                #print('yea')
                store_pre = self.DBh.select(['intention_school_table'], ['block1'], Conditionlist)
                if store_pre is None or store_pre == ''or store_pre == []:
                    count = '1'
                    result_str = count+','+self.score+'.'
                else:
                    #print(store_pre)
                    store = store_pre.split(',')[1][:-1].split('.')  # 记录的列表
                    count = store_pre.split(',')[0]  # 记录人数


                    if int(self.score) < int(store[-1]):
                        store.append(self.score)
                    else:
                        for m in range(len(store)):
                            if int(self.score) >= int(store[m]):
                                store.insert(m,self.score)
                                break
                    count = str(int(count) +1)
                    result_str = count + ','
                    for element in store:
                        result_str = result_str + element + '.'
                self.DBh.update('intention_school_table', ['block1 =' + '\"' + result_str + '\"'], Conditionlist)

            elif int(self.score) < 510:
                store_pre = self.DBh.select(['intention_school_table'], ['block2'], Conditionlist)
                if store_pre is None or store_pre == '' or store_pre == []:
                    count = '1'
                    result_str = count + ',' + self.score + '.'
                else:
                    store = store_pre.split(',')[1][:-1].split('.')  # 记录的列表
                    count = store_pre.split(',')[0]  # 记录人数

                    if int(self.score) < int(store[-1]):
                        store.append(self.score)
                    else:
                        for m in range(len(store)):
                            if int(self.score) >= int(store[m]):
                                store.insert(m,self.score)
                                break
                    count = str(int(count) +1)
                    result_str = count + ','
                    for element in store:
                        result_str = result_str + element + '.'
                self.DBh.update('intention_school_table', ['block2 =' + '\"' + result_str + '\"'], Conditionlist)

            elif int(self.score) < 590:
                store_pre = self.DBh.select(['intention_school_table'], ['block3'], Conditionlist)
                #print(store_pre is None)
                if store_pre is None or store_pre == ''or store_pre == []:
                    count = '1'
                    result_str = count + ',' + self.score + '.'
                else:
                    store = store_pre.split(',')[1][:-1].split('.')  # 记录的列表
                    count = store_pre.split(',')[0]  # 记录人数

                    if int(self.score) < int(store[-1]):
                        store.append(self.score)
                    else:
                        for m in range(len(store)):
                            if int(self.score) >= int(store[m]):
                                store.insert(m,self.score)
                                break
                    count = str(int(count) +1)
                    result_str = count + ','
                    for element in store:
                        result_str = result_str + element + '.'
                self.DBh.update('intention_school_table', ['block3 =' + '\"' + result_str + '\"'], Conditionlist)

            elif int(self.score) < 670:
                store_pre = self.DBh.select(['intention_school_table'], ['block4'], Conditionlist)
                if store_pre is None or store_pre == '' or store_pre == []:
                    count = '1'
                    result_str = count + ',' + self.score + '.'
                else:
                    store = store_pre.split(',')[1][:-1].split('.')  # 记录的列表
                    count = store_pre.split(',')[0]  # 记录人数

                    if int(self.score) < int(store[-1]):
                        store.append(self.score)
                    else:
                        for m in range(len(store)):
                            if int(self.score) >= int(store[m]):
                                store.insert(m,self.score)
                                break
                    count = str(int(count) +1)
                    result_str = count + ','
                    for element in store:
                        result_str = result_str + element + '.'
                self.DBh.update('intention_school_table', ['block4 =' + '\"' + result_str + '\"'], Conditionlist)

            elif int(self.score) < 750:
                store_pre = self.DBh.select(['intention_school_table'], ['block5'], Conditionlist)
                if store_pre is None or store_pre == '' or store_pre == []:
                    count = '1'
                    result_str = count + ',' + self.score + '.'
                else:
                    store = store_pre.split(',')[1][:-1].split('.')  # 记录的列表
                    count = store_pre.split(',')[0]  # 记录人数

                    if int(self.score) < int(store[-1]):
                        store.append(self.score)
                    else:
                        for m in range(len(store)):
                            if int(self.score) >= int(store[m]):
                                store.insert(m,self.score)
                                break
                    count = str(int(count) +1)
                    result_str = count + ','
                    for element in store:
                        result_str = result_str + element + '.'
                self.DBh.update('intention_school_table', ['block5 =' + '\"' + result_str + '\"'], Conditionlist)

            # 对每个学校的每个专业进行修改：
            zhuanye_list = []
            for k in range(len(self.intension_list[0]) - 1):
                k1 = k + 1
                #print(k1)
                zhuanye_list.append(self.intension_list[j][k1])  # 记录j+1学校的专业选择情况
            for l in range(len(zhuanye_list)):  # 对每个专业
                serial = str(l + 1)
                zhuanye_str = zhuanye_list[l]
                Conditionlist = ['schoolID =' + school_str, 'provinceID =' + self.provinceID,
                                 'subject ='  + self.subject  ,'pici =' + self.pici,
                                 'zhuanye=' + zhuanye_str,  # 可能是str，要修改
                                 'serialnumber =' + serial]

                if int(self.score) < 430:
                    store_pre = self.DBh.select(['intension_zhuanye_table'], ['block1'], Conditionlist)
                    if store_pre == None or store_pre == '' or store_pre == []:
                        count = '1'
                        result_str = count + ',' + self.score + '.'
                    else:
                        store = store_pre.split(',')[1][:-1].split('.')  # 记录的列表
                        count = store_pre.split(',')[0]  # 记录人数

                        if int(self.score) < int(store[-1]):
                            store.append(self.score)
                        else:
                            for m in range(len(store)):
                                if int(self.score) >= int(store[m]):
                                    store.insert(m, self.score)
                                    break
                        count = str(int(count) + 1)
                        result_str = count + ','
                        for element in store:
                            result_str = result_str + element + '.'
                    self.DBh.update('intension_zhuanye_table', ['block1 =' + '\"' + result_str + '\"'],
                                    Conditionlist)

                elif int(self.score) < 510:
                    store_pre = self.DBh.select(['intension_zhuanye_table'], ['block2'], Conditionlist)
                    if store_pre == None or store_pre == ''or store_pre == []:
                        count = '1'
                        result_str = count + ',' + self.score + '.'
                    else:
                        store = store_pre.split(',')[1][:-1].split('.')  # 记录的列表
                        count = store_pre.split(',')[0]  # 记录人数

                        if int(self.score) < int(store[-1]):
                            store.append(self.score)
                        else:
                            for m in range(len(store)):
                                if int(self.score) >= int(store[m]):
                                    store.insert(m, self.score)
                                    break
                        count = str(int(count) + 1)
                        result_str = count + ','
                        for element in store:
                            result_str = result_str + element + '.'
                    self.DBh.update('intension_zhuanye_table', ['block2 =' + '\"' + result_str + '\"'],
                                        Conditionlist)

                elif int(self.score) < 590:
                    store_pre = self.DBh.select(['intension_zhuanye_table'], ['block3'], Conditionlist)
                    if store_pre == None or store_pre == ''or store_pre == []:
                        count = '1'
                        result_str = count + ',' + self.score + '.'
                    else:
                        store = store_pre.split(',')[1][:-1].split('.')  # 记录的列表
                        count = store_pre.split(',')[0]  # 记录人数

                        if int(self.score) < int(store[-1]):
                            store.append(self.score)
                        else:
                            for m in range(len(store)):
                                if int(self.score) >= int(store[m]):
                                    store.insert(m, self.score)
                                    break
                        count = str(int(count) + 1)
                        result_str = count + ','
                        for element in store:
                            result_str = result_str + element + '.'
                    self.DBh.update('intension_zhuanye_table', ['block3 =' + '\"' + result_str + '\"'],
                                        Conditionlist)

                elif int(self.score) < 670:
                    store_pre = self.DBh.select(['intension_zhuanye_table'], ['block4'], Conditionlist)
                    if store_pre == None or store_pre == ''or store_pre == []:
                        count = '1'
                        result_str = count + ',' + self.score + '.'
                    else:
                        store = store_pre.split(',')[1][:-1].split('.')  # 记录的列表
                        count = store_pre.split(',')[0]  # 记录人数

                        if int(self.score) < int(store[-1]):
                            store.append(self.score)
                        else:
                            for m in range(len(store)):
                                if int(self.score) >= int(store[m]):
                                    store.insert(m, self.score)
                                    break
                        count = str(int(count) + 1)
                        result_str = count + ','
                        for element in store:
                            result_str = result_str + element + '.'
                    self.DBh.update('intension_zhuanye_table', ['block4 =' + '\"' + result_str + '\"'],
                                        Conditionlist)

                elif int(self.score) < 750:
                    store_pre = self.DBh.select(['intension_zhuanye_table'], ['block5'], Conditionlist)
                    if store_pre == None or store_pre == ''or store_pre == []:
                        count = '1'
                        result_str = count + ',' + self.score + '.'
                    else:
                        store = store_pre.split(',')[1][:-1].split('.')  # 记录的列表
                        count = store_pre.split(',')[0]  # 记录人数

                        if int(self.score) < int(store[-1]):
                            store.append(self.score)
                        else:
                            for m in range(len(store)):
                                if int(self.score) >= int(store[m]):
                                    store.insert(m, self.score)
                                    break
                        count = str(int(count) + 1)
                        result_str = count + ','
                        for element in store:
                            result_str = result_str + element + '.'
                    self.DBh.update('intension_zhuanye_table', ['block5 =' + '\"' + result_str + '\"'],
                                        Conditionlist)
