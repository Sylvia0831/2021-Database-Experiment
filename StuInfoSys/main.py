from tkinter import *
from tkinter import ttk
from menu import *
import time
import getpass
import os
import pymysql
import mysql.connector as sqlc

#sname,sno,cno,scholarship,ssex,sage

def clear_cmd():
    os.system('clear')
def pause_cmd():
    #os.system("pause")
    input("请输入任意键继续...")
    #time.sleep(2)

def show_menu():
    ok = True
    while ok:
        op = '9'
        while op < '0' or op > '8':
            clear_cmd()
            print("\t\t学生信息管理系统")
            print("1 学生信息维护|\t2 课程信息维护|\t3 学生成绩维护")
            print("4 学生成绩统计|\t5 学生成绩排名|\t6 学生信息查询")
            print("7 课程信息查询|\t8 选课信息查询|\t0 退出系统")
            print("请输入您要进行的操作： ")
            op = input()
            if op < '0' or op > '8' :
                print("输入有误，请重新输入")
                pause_cmd()
        if op == '1':
            show_menu_StuInfoModify()
        if op == '2':
            show_menu_CouInfoModify()
        if op == '3':
            show_menu_GradeModify()
        if op == '4':
            analysis_StudentGrade()
        if op == '5':
            StuRank()
        if op == '6':
            show_menu_queryStu()
        if op == '7':
            show_menu_queryCou()
        if op == '8':
            show_menu_querySleCou()
        if op =='0':
            clear_cmd()
            ok= False
#ok
def show_menu_StuInfoModify():
    ok =True
    while ok:
        op='4'
        while op<'0' or op> '3':
            clear_cmd()
            print("\t学生信息维护")
            print("1 添加学生信息\t2 修改学生信息\n3 删除学生信息\t0 返回上级菜单")
            print("请输入您要进行的操作： ")
            op=input()
            if op < '0' or op > '3':
                print("输入有误，请重新输入")
                pause_cmd()
        if op == '1':
            print("请输入学生学号：")
            sno=input()
            while sno.isdigit()==False:
                print("输入有误，请重新输入！\n请输入学生学号：")
                sno = input()
            print("请输入学生姓名：")
            sname=input()
            print("请输入学生性别：")
            ssex=input()
            while ssex!='女' and ssex!='男':
                print("输入有误，请重新输入！\n请输入学生性别：")
                ssex = input()
            print("请输入学生年龄：")
            sage = input()
            while sage<'10' or sage>'80':
                print("年龄有误，请重新输入！\n请输入学生年龄：")
                sage = input()
            print("请输入学生系别：")
            sdept = input()
            print("请输入学生是否获得奖学金：")
            scholarship = input()
            while scholarship != '是' and scholarship != '否':
                print("输入有误，请重新输入！\n请输入学生是否获得奖学金：")
                scholarship = input()
            insert_StudentInfo(sno,sname,ssex,sage,sdept,scholarship)
            print("添加成功！")
            pause_cmd()
        if op == '2':
            print("请输入学生学号：")
            sno = input()
            print("请输入学生姓名：")
            sname = input()
            print("请输入学生性别：")
            ssex = input()
            print("请输入学生年龄：")
            sage = input()
            print("请输入学生系别：")
            sdept = input()
            print("请输入学生是否获得奖学金：")
            scholarship = input()
            update_StudentInfo(sno,sname,ssex,sage,sdept,scholarship)
            print("修改成功！\n修改后该生信息如下：")
            print(query_StuInfo(sno))
            pause_cmd()
        if op == '3':
            print("请输入要删除的学生学号：")
            sno = input()
            cursor = cnx.cursor()
            print("您删除的学生信息如下：")
            query2 = "select * from Student where Sno='%s'" % (sno)
            ret = '%s\t\t%s\t%s\t%s\t%s\t%s\n' % ('Sno', 'Sname', 'Ssex', 'Sage', 'Sdept', 'Scholarship')
            cursor.execute(query2)
            for (Sno, Sname, Ssex, Sage, Sdept, Scholarship) in cursor:
                ret += '%s\t%s\t%s\t%d\t%s\t%s\n' % (Sno, Sname, Ssex, Sage, Sdept, Scholarship)
            print(ret)
            print("请问是否确定删除？(y/n)")
            okk=input();
            if okk=="y" or okk=="Y":
                delete_StuInfo(sno)
                print("删除成功！")
                pause_cmd()
        if op=='0':
            clear_cmd()
            ok=False
#ok
def show_menu_CouInfoModify():
    ok =True
    while ok:
        op='4'
        while op<'0' or op> '3':
            clear_cmd()
            print("\t课程信息维护")
            print("1 添加课程信息\t2 修改课程信息\n3 删除课程信息\t0 返回上级菜单")
            print("请输入您要进行的操作： ")
            op=input()
            if op < '0' or op > '3':
                print("输入有误，请重新输入")
                pause_cmd()
        if op == '1':
            print("请输入课程号：")
            cno = input()
            while cno.isdigit() == False:
                print("输入有误，请重新输入！\n请输入课程：")
                cno = input()
            print("请输入课程名：")
            cname = input()
            print("请输入先修课程号：")
            cpno = input()
            while cno.isdigit() == False:
                print("输入有误，请重新输入！\n请输入先修课程号：")
                cno = input()
            print("请输入课程学分：")
            ccredit = input()
            insert_CourseInfo(cno, cname, cpno, ccredit)
            print("添加成功！")
            pause_cmd()
        if op == '2':
            print("请输入课程号：")
            cno = input()
            print("请输入课程名：")
            cname = input()
            print("请输入先修课程号：")
            cpno = input()
            print("请输入课程学分：")
            ccredit = input()
            update_CourseInfo(cno,cname,cpno,ccredit)
            print("修改成功！\n修改后该课程信息如下：")
            cursor = cnx.cursor()
            query = "select * from Course where cno ='%s'" %(cno)
            ret = '%s\t%s\t\t%s\t%s\n' % ('Cno', 'Cname', 'Cpno', 'Ccredit')
            cursor.execute(query)
            for (Cno, Cname, Cpno, Ccredit) in cursor:
                ret += '%s\t%s\t%s\t%s\n' % (Cno, Cname, Cpno, Ccredit)
            print(ret)
            pause_cmd()
        if op == '3':
            print("所有未被选课的课程如下：")
            cursor = cnx.cursor()
            # 显示全部未选课的课程信息
            query = "select * from course where cno not in (select distinct cno from sc )"
            cursor.execute(query)
            ret = '%s\t%s\t\t%s\t%s\n' % ('Cno', 'Cname', 'Cpno', 'Ccredit')
            for (Cno, Cname, Cpno, Ccredit) in cursor:
                ret += '%s\t%s\t%s\t%s\n' % (Cno, Cname, Cpno, Ccredit)
            print(ret)
            print("是否确认删除上述这些课程？(y/n)")
            okk=input()
            if okk=="y" or okk=="Y":
                delete_Course()
                print("删除成功！")
        if op=='0':
            clear_cmd()
            ok=False
#ok
def show_menu_GradeModify():
    ok =True
    while ok:
        op='4'
        while op<'0' or op> '2':
            clear_cmd()
            print("\t\t学生成绩维护")
            print("1 添加学生成绩\t2 修改学生成绩\t0 返回上级菜单")
            print("请输入您要进行的操作： ")
            op=input()
            if op < '0' or op > '2':
                print("输入有误，请重新输入")
                pause_cmd()
        if op == '1':
            print("请输入学生学号：")
            sno = input()
            while sno.isdigit() == False:
                print("输入有误，请重新输入！\n请输入学生学号：")
                sno = input()
            print("请输入课程号：")
            cno = input()
            while cno.isdigit() == False:
                print("输入有误，请重新输入！\n请输入课程号：")
                cno = input()
            print("请输入成绩：")
            grade = input()
            while int(grade) < 0 or int(grade) > 100:
                print("输入有误，请重新输入！\n请输入成绩：")
                grade = input()
            insert_Grade(sno, cno, grade)
            print("添加成功！")
            pause_cmd()
        if op == '2':
            print("请输入学生学号：")
            sno = input()
            print("请输入课程号：")
            cno = input()
            print("请输入成绩：")
            grade = input()
            while int(grade) < 0 or int(grade) > 100:
                 print("输入有误，请重新输入！\n请输入成绩：")
                 grade = input()
            update_Grade(sno, cno, grade)
            print("修改成功！\n修改后成绩如下：")
            ret = '%s\t\t%s\t%s\n' % ('Sno', 'Cno', 'Grade')
            ret += '%s\t%s\t%s\n' % (sno, cno, grade)
            print(ret)
            pause_cmd()
        if op=='0':
            clear_cmd()
            ok=False

#ok
def show_menu_queryStu():
    ok = True
    while ok:
        op = '3'
        while op < '0' or op > '2':
            clear_cmd()
            print("\t\t学生成绩查询")
            print("1 查询所有学生信息\t2 按学号查询学生信息\t0 返回上级菜单")
            print("请输入您要进行的操作： ")
            op = input()
            if op < '0' or op > '2':
                print("输入有误，请重新输入")
                pause_cmd()
        if op == '1':
            ret = query_AllStudentInfo()
            print(ret)
            #input("请输入任意键继续...")
            pause_cmd()
        if op == '2':
            print("请输入您要查询的学生学号：")
            sno = input()
            ret="学号为%s的学生信息：\n" %(sno)
            ret+= query_StuInfo(sno)
            ret+="\n学号为%s的学生课程成绩信息：\n" %(sno)
            ret+=query_StuCouInfo(sno)

            if ret.find("False",0,len(ret)) != -1:
                print("查询的学生信息不存在")
            else:
                print(ret)
                # pause_cmd()
            pause_cmd()
        if op == '0':
            clear_cmd()
            ok = False
#ok
def show_menu_queryCou():
    ok = True
    while ok:
        op = '2'
        while op < '0' or op > '1':
            clear_cmd()
            print("\t课程信息查询")
            print("1 查询所有课程信息\t0 返回上级菜单")
            print("请输入您要进行的操作： ")
            op = input()
            if op < '0' or op > '1':
                print("输入有误，请重新输入")
                pause_cmd()
        if op == '1':
            ret = query_AllCourseInfo()
            print(ret)
            pause_cmd()
        if op == '0':
            clear_cmd()
            ok = False
#ok
def show_menu_querySleCou():
    ok = True
    while ok:
        op = '2'
        while op < '0' or op > '1':
            clear_cmd()
            print("\t选课信息查询")
            print("1 查询所有选课信息\t0 返回上级菜单")
            print("请输入您要进行的操作： ")
            op = input()
            if op < '0' or op > '1':
                print("输入有误，请重新输入")
                pause_cmd()
        if op == '1':
            ret = query_AllCourseSelectInfo()
            print(ret)
            pause_cmd()
        if op == '0':
            clear_cmd()
            ok = False
#ok
# 连接数据库
def login():
    clear_cmd()
    global cnx
    print("\t\t欢迎使用学生信息管理系统\t\t")
    print("请输入用户名：")
    username=input()
    password=getpass.getpass('请输入密码：')
   # print("请输入密码")

    try:
        cnx = sqlc.connect(user=username,
                           password=password,
                           host='localhost',
                           database='S_T_U201911658')
    except sqlc.Error:
        return False
    return cnx


# 查询
# 查询所有学生基本信息
def query_AllStudentInfo():
    cursor = cnx.cursor()
    query = 'select * from Student'
    ret = '%s\t\t%s\t%s\t%s\t%s\t%s\n' % ('Sno', 'Sname', 'Ssex', 'Sage', 'Sdept', 'Scholarship')
    cursor.execute(query)
    for (Sno, Sname, Ssex, Sage, Sdept, Scholarship) in cursor:
        ret += '%s\t%s\t%s\t%d\t%s\t%s\n' % (Sno, Sname, Ssex, Sage, Sdept, Scholarship)
    return ret

# 查询所有课程信息
def query_AllCourseInfo():
    cursor = cnx.cursor()
    query = 'select * from Course'
    ret = '%s\t%s\t\t%s\t%s\n' % ('Cno', 'Cname', 'Cpno', 'Ccredit')
    cursor.execute(query)
    for (Cno, Cname, Cpno, Ccredit) in cursor:
        ret += '%s\t%s\t%s\t%s\n' % (Cno, Cname, Cpno, Ccredit)
    return ret

# 查询所有选课信息
def query_AllCourseSelectInfo():
    cursor = cnx.cursor()
    query = 'select * from SC'
    ret = '%s\t\t%s\t%s\n' % ('Sno', 'Cno', 'Grade')
    cursor.execute(query)
    for (Sno, Cno, Grade) in cursor:
        ret += '%s\t%s\t%s\n' % (Sno, Cno, Grade)
    return ret

# 按学号查询学生信息
def query_StuInfo(id):
    cursor = cnx.cursor()
    try:
        query = 'select * from Student where Sno=' + '\'' + id + '\''
        ret = '%s\t\t%s\t%s\t%s\t%s\t%s\n' % ('Sno', 'Sname', 'Ssex', 'Sage', 'Sdept', 'Scholarship')
        len1=len(ret)
        cursor.execute(query)
        for (Sno, Sname, Ssex, Sage, Sdept, Scholarship) in cursor:
            ret += '%s\t%s\t%s\t%d\t%s\t%s\n' % (Sno, Sname, Ssex, Sage, Sdept, Scholarship)
    except sqlc.Error:
        return "False"
    if len1==len(ret):
        return "False"
    else:
        return ret

# 按学号查询学生选课信息
def query_StuCouInfo(id):
    cursor = cnx.cursor()
    query = 'select student.sname,student.sno,course.cno,course.cname,sc.grade '
    query += 'from sc,student,course '
    query += 'where student.sno=sc.sno and sc.cno=course.cno and student.sno=' + '\'' + id + '\''
    ret = '%s\t%s\t\t%s\t%s\t\t%s\n' % ('Sname', 'Sno', 'Cno', 'Cname', 'Grade')
    cursor.execute(query)
    for (Sname, Sno, Cno, Cname, Grade) in cursor:
        ret += '%s\t%s\t%s\t%s\t%s\n' % (Sname, Sno, Cno, Cname, Grade)
    return ret
# 插入与更新
# 插入学生信息
def insert_StudentInfo(sno, sname, ssex, sage, sdept, scholarship):
    cursor = cnx.cursor()
    query = "insert into Student values('%s', '%s', '%s', '%s', '%s', '%s')" \
            % (sno, sname, ssex, sage, sdept, scholarship)
    #print(query)
    try:
        cursor.execute(query)
    except sqlc.Error:
        return False
    return True
# 修改学生信息
def update_StudentInfo(sno, sname, ssex, sage, sdept, scholarship):
    # cursor = cnx.cursor()
    if len(sno) == 0:
        return False
    try:
        if len(sname):
            cursor = cnx.cursor()
            query = "update Student set Sname = '%s' where Sno = '%s'" % (sname, sno)
            cursor.execute(query)
            cursor.close()
        if len(ssex):
            cursor = cnx.cursor()
            query = "update Student set ssex = '%s' where Sno = '%s'" % (ssex, sno)
            cursor.execute(query)
            cursor.close()
        if len(sage):
            cursor = cnx.cursor()
            query = "update Student set sage = %s where Sno = '%s'" % (sage, sno)
            cursor.execute(query)
            cursor.close()
        if len(sdept):
            cursor = cnx.cursor()
            query = "update Student set sdept = '%s' where Sno = '%s'" % (sdept, sno)
            cursor.execute(query)
            cursor.close()
        if len(scholarship):
            cursor = cnx.cursor()
            query = "update Student set Scholarship = '%s' where Sno = '%s'" % (scholarship, sno)
            cursor.execute(query)
            cursor.close()
    except sqlc.Error:
        print("error")
        return False
    return True
#删除学生信息
def delete_StuInfo(sno):
    cursor = cnx.cursor()
    query = "delete from Student where sno='%s'" % (sno)
    #print(query)
    try:
        cursor.execute(query)
    except sqlc.Error:
        return False
    return True

# 增加课程信息
def insert_CourseInfo(cno, cname, cpno, ccredit):
    cursor = cnx.cursor()
    query = "insert into Course values('%s', '%s', '%s', '%s')" \
            % (cno, cname, cpno, ccredit)
   # print(query)
    try:
        cursor.execute(query)
    except sqlc.Error:
        return False
    return True
# 修改课程信息
def update_CourseInfo(cno, cname, cpno, ccredit):
    # cursor = cnx.cursor()
    if len(cno) == 0:
        return False
    # 补充显示提示是否确认修改该门课程
    try:
        if len(cname):
            cursor = cnx.cursor()
            query = "update Course set Cname = '%s' where Cno = '%s'" % (cname, cno)
            cursor.execute(query)
            cursor.close()
        if len(cpno):
            cursor = cnx.cursor()
            query = "update Course set Cpno = '%s' where Cno = '%s'" % (cpno, cno)
            cursor.execute(query)
            cursor.close()
        if len(ccredit):
            cursor = cnx.cursor()
            query = "update Course set Ccredit = %s where Cno = '%s'" % (ccredit, cno)
            cursor.execute(query)
            cursor.close()
    except sqlc.Error:
        print("error")
        return False
    return True
# 删除无选课的课程信息
def delete_Course():
    cursor = cnx.cursor()
    query = "delete from course where cno not in (select distinct cno from sc )"
    try:
        cursor.execute(query)
    except sqlc.Error:
        return False
    return True

# 插入学生成绩
def insert_Grade(sno, cno, grade):
    cursor = cnx.cursor()
    query = "insert into sc values('%s', '%s', '%s')" \
            % (sno, cno, grade)
  #  print(query)
    try:
        cursor.execute(query)
    except sqlc.Error:
        return False
    return True


# 修改学生成绩
def update_Grade(sno, cno, grade):
    # cursor = cnx.cursor()
    if len(sno) == 0:
        return False
    # 补充显示提示是否确认修改该门课程
    try:
        if len(cno):
            cursor = cnx.cursor()
            query = "update sc set Cno = '%s' where sno = '%s'" % (cno, sno)
            cursor.execute(query)
            cursor.close()
        if len(grade):
            cursor = cnx.cursor()
            query = "update sc set grade = '%s' where sno = '%s'" % (grade, sno)
            cursor.execute(query)
            cursor.close()
    except sqlc.Error:
        print("error")
        return False
    return True


# 统计学生平均成绩、最高分、最低分、优秀率、不及格人数
def analysis_StudentGrade():
    clear_cmd()
    cursor = cnx.cursor()
    depts=[]
    depts2=[]
    total=[]
    good=[]
    bad=[]

    print("各系平均成绩，最高分，最低分：")
    query = " select sdept,avg(grade) as avgg,max(grade) as maxx,min(grade) as minn from sc,student where student.sno=sc.sno group by sdept"
    cursor.execute(query)
    ret = '%s\t%s\t%s\t%s\n' % ("Sdept", "AvgGrade", "MaxGrade", "MinGrade")
    for (sdept, avgg, maxx, minn) in cursor:
        ret += '%s\t%s\t\t%s\t\t%s\n' % (sdept, avgg, maxx, minn)
    print(ret)
    query = "select sdept,count(*) as cn from sc,student where sc.sno=student.sno group by sdept"
    cursor.execute(query)
    for (sdept,cn) in cursor:
        depts.append(sdept)
        total.append(float(cn))

    query="select sdept,count(*) as cn from sc,student where sc.sno=student.sno and grade>=90 group by sdept"
    cursor.execute(query)
    for (sdept,cn) in cursor:
        good.append(float(cn))
    print("各系优秀率：")
    print("Sdept\tRate")
    for i in range(len(depts)):
        tmp=(good[i]/total[i])*100
        tmp=round(tmp,1)
        print(depts[i]+"\t"+str(tmp)+"%")
    query = "select sdept,count(*) as cn from sc,student where sc.sno=student.sno and grade<90 group by sdept"
    cursor.execute(query)
    for (sdept, cn) in cursor:
        depts2.append(sdept)
        bad.append(cn)
    print("各系不及格人数：")
    print("Sdept\tNumber")
    for i in range(len(depts2)):
        print(depts[i] + "\t" + str(bad[i]))
    pause_cmd()
def StuRank():
    clear_cmd()
    depts=[]
    cursor = cnx.cursor()
    query = " select distinct sdept from student "
    cursor.execute(query)
    for (sdept) in cursor:
        a="%s"%(sdept)
        depts.append(a)
    cursor = cnx.cursor()
    ret=''
    for i in range(len(depts)):
        query = " select sc.Sno,Cno,Grade from sc,student where Sdept='%s' and sc.sno=student.sno order by grade  desc"%(depts[i])
        #print(query)
        cursor.execute(query)
        ret+="\n%s\n"%(depts[i])
        ret += '%s\t\t%s\t%s\t\n' % ("Sno", "Cno", "Grade")
        for (sno,cno,grade) in cursor:
            ret += '%s\t%s\t%s\n' % (sno,cno,grade)
    print(ret)
    pause_cmd()

def main():

    try:
        show_menu()
        print("\t已退出")
    except RuntimeError:
        print("\t连接失败，请重试")
    finally:
        cnx.close()

cnx=login()
while cnx==False:
    print("用户名或密码错误，请重新登录")
    pause_cmd()
    cnx=login()
print("登录成功")
pause_cmd()
main()
# query = "select sdept,count(*) from sc,student where student.sno=sc.sno and grade>=90 group by sdept;"


# root = Tk()
# root.title("Student Management System")
# winWidth = 600
# winHeight = 420
# screenWidth = root.winfo_screenwidth()
# screenHeight = root.winfo_screenheight()
#
# x = int((screenWidth - winWidth) / 2)
# y = int((screenHeight - winHeight) / 2)
# root.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
# root.resizable(False, False)
#
# frame = ttk.Frame(root)
# frame.place(rely=.5, relx=0.5, x=-122.5, y=-100, width=245, height=200)
# # 返回参数信息
# print(frame.place_info())
# ttk.Label(frame, text="用户名").grid(row=0)
# ttk.Label(frame, text="密码").grid(row=1)
# username_var = StringVar()
# pwd_var = StringVar()
# ttk.Entry(frame, textvariable = username_var).grid(row=0, column=1)
# ttk.Entry(frame, show="*", textvariable=pwd_var).grid(row=1, column=1)
# ttk.Label(frame).grid(row=0, rowspan=2, column=2, padx=5, pady=5)
# ttk.Button(frame, text="登录", command=loginn(username_var,pwd_var)).grid(row=2, columnspan=3)
#
# root.mainloop()
