from tkinter import *
import tkinter
import tkinter.messagebox
import mysql.connector as sqlc

def exitt():
    tkinter.messagebox.showinfo('再见', '欢迎下次使用！bye～')
    cnx.commit()
    cnx.close()
    root.destroy()
#
def show_menu():
    menuframe = Frame(root)
    menuframe.place(rely=.4, relx=0.4, x=-122.5,y=-100, width=500, height=400)
    Button(menuframe, text="学生信息维护", command=show_menu_StuInfoModify).grid(row=0,column=0)
    Button(menuframe, text="课程信息维护", command=show_menu_CouInfoModify).grid(row=0,column=2)
    Button(menuframe, text="学生成绩维护", command=show_menu_GradeModify).grid(row=2, column=0)
    Button(menuframe, text="学生成绩统计", command=analysis_StudentGrade).grid(row=2, column=2)
    Button(menuframe, text="学生成绩排名", command=StuRank).grid(row=4, column=0)
    Button(menuframe, text="学生信息查询", command=show_menu_queryStu).grid(row=4, column=2)
    Button(menuframe, text="课程信息查询", command=show_menu_queryCou).grid(row=6, column=0)
    Button(menuframe, text="选课信息查询", command=show_menu_querySleCou).grid(row=6, column=2)
    Button(menuframe, text="退出系统", command=exitt).grid(row=7,column=1)
def show_menu_StuInfoModify():
    menuframe1 = Frame(root)
    menuframe1.place(rely=.3, relx=0.3, x=-122.5,y=-100, width=500, height=400)
    Button(menuframe1, text="添加学生信息", command=insert_StudentInfo).place(relx=0.3,rely=0.1)
    Button(menuframe1, text="修改学生信息", command=update_StudentInfo).place(relx=0.3,rely=0.2)
    Button(menuframe1, text="删除学生信息", command=delete_StuInfo).place(relx=0.3,rely=0.3)
    Button(menuframe1, text="返回上级菜单", command=show_menu).place(relx=0.3,rely=0.4)
    Button(menuframe1, text="退出系统", command=exitt).place(relx=0.3,rely=0.5)
def show_menu_CouInfoModify():
    menuframe1 = Frame(root)
    menuframe1.place(rely=.3, relx=0.3, x=-122.5,y=-100, width=500, height=400)
    Button(menuframe1, text="添加课程信息", command=insert_CourseInfo).place(relx=0.3, rely=0.1)
    Button(menuframe1, text="修改课程信息", command=update_CourseInfo).place(relx=0.3, rely=0.2)
    Button(menuframe1, text="删除课程信息", command=delete_Course).place(relx=0.3, rely=0.3)
    Button(menuframe1, text="返回上级菜单", command=show_menu).place(relx=0.3, rely=0.4)
    Button(menuframe1, text="退出系统", command=exitt).place(relx=0.3, rely=0.5)

def show_menu_GradeModify():
    menuframe1 = Frame(root)
    menuframe1.place(rely=.3, relx=0.3, x=-122.5,y=-100, width=500, height=400)
    Button(menuframe1, text="添加学生成绩", command=insert_Grade).place(relx=0.3, rely=0.1)
    Button(menuframe1, text="修改学生成绩", command=update_Grade).place(relx=0.3, rely=0.2)
    Button(menuframe1, text="返回上级菜单", command=show_menu).place(relx=0.3, rely=0.3)
    Button(menuframe1, text="退出系统", command=exitt).place(relx=0.3, rely=0.4)
#
def show_menu_queryStu():
    menuframe1 = Frame(root)
    menuframe1.place(rely=.3, relx=0.3, x=-122.5,y=-100, width=500, height=400)
    Button(menuframe1, text="查询所有学生信息", command=query_AllStudentInfo).place(relx=0.3, rely=0.1)
    Button(menuframe1, text="按学号查询学生信息", command=query_StuInfo).place(relx=0.3, rely=0.2)
    Button(menuframe1, text="返回上级菜单", command=show_menu).place(relx=0.3, rely=0.3)
    Button(menuframe1, text="退出系统", command=exitt).place(relx=0.3, rely=0.4)
#
def show_menu_queryCou():
    menuframe1 = Frame(root)
    menuframe1.place(rely=.3, relx=0.3, x=-122.5,y=-100, width=500, height=400)
    Button(menuframe1, text="查询所有课程信息", command=query_AllCourseInfo).place(relx=0.3, rely=0.1)
    Button(menuframe1, text="返回上级菜单", command=show_menu).place(relx=0.3, rely=0.2)
    Button(menuframe1, text="退出系统", command=exitt).place(relx=0.3, rely=0.3)
def show_menu_querySleCou():
    menuframe1 = Frame(root)
    menuframe1.place(rely=.3, relx=0.3, x=-122.5,y=-100, width=500, height=400)
    Button(menuframe1, text="查询所有课程信息", command=query_AllCourseSelectInfo).place(relx=0.3, rely=0.1)
    Button(menuframe1, text="返回上级菜单", command=show_menu).place(relx=0.3, rely=0.2)
    Button(menuframe1, text="退出系统", command=exitt).place(relx=0.3, rely=0.3)
#
# 连接数据库
#
def login():
    global cnx
    username=inusername.get()
    password=inpwd.get()

    try:
        cnx = sqlc.connect(user=username,
                           password=password,
                           host='localhost',
                           database='S_T_U201911658')
    except sqlc.Error:
        tkinter.messagebox.showerror('登录失败', '用户名或密码错误！\n请重新登录！')
        return False
    tkinter.messagebox.showinfo('登录成功', '欢迎使用学生信息管理系统！')
    frame.destroy()
    show_menu()
    return cnx
# 查询
# 查询所有学生基本信息
def query_AllStudentInfo():
    menuframe = Frame(root)
    menuframe.place(rely=.3, relx=0.3, x=-122.5,y=-100, width=500, height=400)
    cursor = cnx.cursor()
    query = 'select * from Student'
    ret = '%s\t%s\t%s\t%s\t%s\t%s\n' % ('Sno', 'Sname', 'Ssex', 'Sage', 'Sdept', 'Scholarship')
    cursor.execute(query)
    for (Sno, Sname, Ssex, Sage, Sdept, Scholarship) in cursor:
        ret += '%s\t%s\t%s\t%d\t%s\t%s\n' % (Sno, Sname, Ssex, Sage, Sdept, Scholarship)
    w1 = Message(menuframe, text=ret, width=600).grid(row=1, column=0)
    Button(menuframe, text="返回上一级",
               command=show_menu_queryStu).grid(row=2, column=0)
# 查询所有课程信息
def query_AllCourseInfo():
    cursor = cnx.cursor()
    query = 'select * from Course'
    ret = '%s\t%s\t%s\t%s\n' % ('Cno', 'Cname', 'Cpno', 'Ccredit')
    cursor.execute(query)
    for (Cno, Cname, Cpno, Ccredit) in cursor:
        ret += '%s\t%s\t%s\t%s\n' % (Cno, Cname, Cpno, Ccredit)
    menuframe = Frame(root)
    menuframe.place(rely=.3, relx=0.3, x=-122.5,y=-100, width=500, height=400)
    w1 = Message(menuframe, text=ret, width=500).grid(row=0, column=0)
    Button(menuframe, text="返回上一级",
               command=show_menu_queryCou).grid(row=1, column=0)
# 查询所有选课信息
def query_AllCourseSelectInfo():
    cursor = cnx.cursor()
    query = 'select * from SC'
    ret = '%s\t%s\t%s\n' % ('Sno', 'Cno', 'Grade')
    cursor.execute(query)
    for (Sno, Cno, Grade) in cursor:
        ret += '%s\t%s\t%s\n' % (Sno, Cno, Grade)
    menuframe = Frame(root)
    menuframe.place(rely=.3, relx=0.3, x=-122.5,y=-100, width=500, height=400)
    w1 = Message(menuframe, text=ret, width=500).grid(row=0, column=0)
    Button(menuframe, text="返回上一级",
               command=show_menu_querySleCou).grid(row=1, column=0)
# 按学号查询学生信息
def query_StuInfo_button(sno):
    menuframe = Frame(root)
    menuframe.place(rely=.3, relx=0.3, x=-122.5,y=-100, width=500, height=400)
    cursor = cnx.cursor()
    try:
        query = 'select * from Student where Sno=' + '\'' + sno + '\''
        ret = '\n学号%s的学生基本信息如下：\n' %(sno)
        ret += '%s\t%s\t%s\t%s\t%s\t%s\n' % ('Sno', 'Sname', 'Ssex', 'Sage', 'Sdept', 'Scholarship')
        len1 = len(ret)
        cursor.execute(query)
        for (Sno, Sname, Ssex, Sage, Sdept, Scholarship) in cursor:
            ret += '%s\t%s\t%s\t%d\t%s\t%s\n' % (Sno, Sname, Ssex, Sage, Sdept, Scholarship)
        query = 'select student.sname,student.sno,course.cno,course.cname,sc.grade '
        query += 'from sc,student,course '
        query += 'where student.sno=sc.sno and sc.cno=course.cno and student.sno=' + '\'' + sno + '\''
        ret+='\n学号%s的学生选课信息如下：\n' %(sno)
        ret += '%s\t%s\t%s\t%s\t%s\n' % ('Sname', 'Sno', 'Cno', 'Cname', 'Grade')
        cursor.execute(query)
        for (Sname, Sno, Cno, Cname, Grade) in cursor:
            ret += '%s\t%s\t%s\t%s\t%s\n' % (Sname, Sno, Cno, Cname, Grade)
        w1 = Message(menuframe, text=ret, width=500).grid(row=0, column=0)

    except sqlc.Error:
        tkinter.messagebox.showinfo('提示', '查询失败！')
    if len1 == len(ret):
        tkinter.messagebox.showinfo('提示', '查询失败')
    Button(menuframe, text="返回上一级", command=show_menu_queryStu).grid(row=1, column=0)

def query_StuInfo():
    menuframe = Frame(root)
    menuframe.place(rely=.3, relx=0.3, x=-122.5,y=-100, width=500, height=400)
    Label(menuframe, text="请输入学号").grid(row=0, column=0)
    sno = Entry(menuframe)
    sno.grid(row=0, column=1)
    Button(menuframe, text="查询",
               command=lambda:query_StuInfo_button(sno.get())).grid(row=2, column=1)

# 插入与更新
# 插入学生信息
#
def insert_StudentInfo_button(sno,sname,sage,ssex,sdept,scholarship):
    cursor = cnx.cursor()
    query = "insert into Student values('%s', '%s', '%s', '%s', '%s', '%s')" \
            % (sno, sname, ssex, sage, sdept, scholarship)
    try:
        cursor.execute(query)

    except sqlc.Error:
        tkinter.messagebox.showinfo('失败', '该学生信息插入失败！')
        return False
    tkinter.messagebox.showinfo('成功', '该学生信息插入成功！')
    cnx.commit()
    show_menu_StuInfoModify()
#
def insert_StudentInfo():
    menuframe = Frame(root)
    menuframe.place(rely=.4, relx=0.4, x=-122.5,y=-100, width=500, height=400)
    Label(menuframe, text="学号").grid(row=0, column=0)
    snoo = Entry(menuframe)
    snoo.grid(row=0, column=1)
    Label(menuframe, text="姓名").grid(row=1, column=0)
    snamee = Entry(menuframe)
    snamee.grid(row=1, column=1)

    Label(menuframe, text="性别").grid(row=2, column=0)
    var = IntVar()
    rd1 = Radiobutton(menuframe, text="男", variable=var, value=0).grid(row=2,column=1)
    rd2 = Radiobutton(menuframe, text="女", variable=var, value=1).grid(row=2,column=2)
    dic = {0: '男', 1: '女'}
    Label(menuframe, text="年龄").grid(row=3, column=0)
    sagee = Entry(menuframe)
    sagee.grid(row=3, column=1)
    Label(menuframe, text="系别").grid(row=4, column=0)
    sdeptt = Entry(menuframe)
    sdeptt.grid(row=4, column=1)
    Label(menuframe, text="奖学金").grid(row=5, column=0)
    varr = IntVar()
    rd11 = Radiobutton(menuframe, text="是", variable=varr, value=0).grid(row=5,column=1)
    rd22 = Radiobutton(menuframe, text="否", variable=varr, value=1).grid(row=5,column=2)
    dicc = {0: '是', 1: '否'}
    Button(menuframe, text="确定", command=lambda:insert_StudentInfo_button(snoo.get(), snamee.get(), sagee.get(), dic.get(var.get()), sdeptt.get(),
                                                         dicc.get(varr.get()))).grid(row=6, column=1)
# 修改学生信息
#
def update_StudentInfo_button(sno, sname, sage, ssex, sdept, scholarship):
    try:
        if len(sname):
            cursor = cnx.cursor()
            query = "update Student set Sname = '%s' where Sno = '%s'" % (sname, sno)
            cursor.execute(query)
            cursor.close()

        if len(ssex) and ssex!='不修改':
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
        if len(scholarship) and scholarship!='不修改':
            cursor = cnx.cursor()
            query = "update Student set Scholarship = '%s' where Sno = '%s'" % (scholarship, sno)
            cursor.execute(query)
            cursor.close()
    except sqlc.Error:
        tkinter.messagebox.showinfo('修改失败', '该学生信息修改失败！')
        return False
    cursor = cnx.cursor()

    query = 'select * from Student where Sno=' + '\'' + sno + '\''
    cursor.execute(query)
    for (Sno, Sname, Ssex, Sage, Sdept, Scholarship) in cursor:
        ret = '%s\t%s\t%s\t%d\t%s\t%s\n' % (Sno, Sname, Ssex, Sage, Sdept, Scholarship)
    tkinter.messagebox.showinfo('修改成功', '该学生信息修改后如下：\n'+ret)
    cnx.commit()
    show_menu_StuInfoModify()
#
def update_StudentInfo():
    menuframe = Frame(root)
    menuframe.place(rely=.4, relx=0.4, x=-122.5,y=-100, width=500, height=400)
    Label(menuframe, text="学号").grid(row=0, column=0)
    snoo = Entry(menuframe)
    snoo.grid(row=0, column=1)
    Label(menuframe, text="姓名").grid(row=1, column=0)
    snamee = Entry(menuframe)
    snamee.grid(row=1, column=1)
    Label(menuframe, text="性别").grid(row=2, column=0)
    var = IntVar()
    rd1 = Radiobutton(menuframe, text="男", variable=var, value=0).grid(row=2, column=1)
    rd2 = Radiobutton(menuframe, text="女", variable=var, value=1).grid(row=2, column=2)
    rd3 = Radiobutton(menuframe, text="不修改", variable=var, value=2).grid(row=2, column=3)
    dic = {0: '男', 1: '女',2:'不修改'}
    Label(menuframe, text="年龄").grid(row=3, column=0)
    sagee = Entry(menuframe)
    sagee.grid(row=3, column=1)
    Label(menuframe, text="系别").grid(row=4, column=0)
    sdeptt = Entry(menuframe)
    sdeptt.grid(row=4, column=1)
    Label(menuframe, text="奖学金").grid(row=5, column=0)
    varr = IntVar()
    rd11 = Radiobutton(menuframe, text="是", variable=varr, value=0).grid(row=5, column=1)
    rd22 = Radiobutton(menuframe, text="否", variable=varr, value=1).grid(row=5, column=2)
    rd22 = Radiobutton(menuframe, text="不修改", variable=varr, value=2).grid(row=5, column=3)
    dicc = {0: '是', 1: '否',2:'不修改'}
    Button(menuframe, text="确定",
               command=lambda: update_StudentInfo_button(snoo.get(), snamee.get(), sagee.get(), dic.get(var.get()), sdeptt.get(),
                                                         dicc.get(varr.get()))).grid(row=6, column=1)
#
def delete_StuInfo_button(sno):
    cursor = cnx.cursor()
    query2 = "select * from Student where Sno='%s'" % (sno)
    cursor.execute(query2)
    for (Sno, Sname, Ssex, Sage, Sdept, Scholarship) in cursor:
        ret = '%s\t%s\t%s\t%d\t%s\t%s\n' % (Sno, Sname, Ssex, Sage, Sdept, Scholarship)
    a = tkinter.messagebox.askokcancel('提示', '该学生信息如下：\n'+ret+'\n您确定要删除吗')
    if a==True:
        cursor = cnx.cursor()
        query = "delete from Student where sno='%s'" % (sno)
        try:
            cursor.execute(query)
        except sqlc.Error:
            tkinter.messagebox.showinfo('提示', '删除失败！')
            show_menu_StuInfoModify()
            return False
        tkinter.messagebox.showinfo('提示', '删除成功！')
    cnx.commit()
    show_menu_StuInfoModify()
#删除学生信息
#
def delete_StuInfo():
    menuframe = Frame(root)
    menuframe.place(rely=.4, relx=0.4, x=-122.5,y=-100, width=500, height=400)
    Label(menuframe, text="学号").grid(row=0, column=0)
    snoo = Entry(menuframe)
    snoo.grid(row=0, column=2)
    Button(menuframe, text="确定",command=lambda: delete_StuInfo_button(snoo.get())).grid(row=2, column=1)
# 增加课程信息
#
def insert_CourseInfo_button(cno, cname, cpno, ccredit):
    cursor = cnx.cursor()
    query = "insert into Course values('%s', '%s', '%s', '%s')" \
            % (cno, cname, cpno, ccredit)
    try:
        cursor.execute(query)
    except sqlc.Error:
        tkinter.messagebox.showinfo('失败', '该课程信息插入失败！')
        show_menu_StuInfoModify()
        return False
    tkinter.messagebox.showinfo('成功', '该课程信息插入成功！')
    cnx.commit()
    show_menu_CouInfoModify()
#ok
def insert_CourseInfo():
    menuframe = Frame(root)
    menuframe.place(rely=.4, relx=0.4, x=-122.5,y=-100, width=500, height=400)
    Label(menuframe, text="课程号").grid(row=0, column=0)
    cno = Entry(menuframe)
    cno.grid(row=0, column=1)
    Label(menuframe, text="课程名").grid(row=1, column=0)
    cname = Entry(menuframe)
    cname.grid(row=1, column=1)
    Label(menuframe, text="先修课程号").grid(row=2, column=0)
    cpno = Entry(menuframe)
    cpno.grid(row=2, column=1)

    Label(menuframe, text="学分").grid(row=3, column=0)
    ccredit = Entry(menuframe)
    ccredit.grid(row=3, column=1)
    Button(menuframe, text="确定",
               command=lambda: insert_CourseInfo_button(cno.get(), cname.get(), cpno.get(),ccredit.get())).grid(row=5, column=1)
# 修改课程信息
def update_CourseInfo_button(cno, cname, cpno, ccredit):
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
        tkinter.messagebox.showinfo('修改失败', '该课程信息修改失败！')
        show_menu_CouInfoModify()
        return False
    cursor = cnx.cursor()
    query = "select * from Course where cno ='%s'" % (cno)
    cursor.execute(query)
    for (Cno, Cname, Cpno, Ccredit) in cursor:
        ret = '%s\t%s\t%s\t%s\n' % (Cno, Cname, Cpno, Ccredit)
    tkinter.messagebox.showinfo('修改成功', '该课程信息修改后如下：\n'+ret)
    cnx.commit()
    show_menu_CouInfoModify()
#
def update_CourseInfo():
    menuframe = Frame(root)
    menuframe.place(rely=.4, relx=0.4, x=-122.5,y=-100, width=500, height=400)
    Label(menuframe, text="课程号").grid(row=0, column=0)
    cno = Entry(menuframe)
    cno.grid(row=0, column=1)
    Label(menuframe, text="课程名").grid(row=1, column=0)
    cname = Entry(menuframe)
    cname.grid(row=1, column=1)

    Label(menuframe, text="先修课程号").grid(row=2, column=0)
    cpno = Entry(menuframe)
    cpno.grid(row=2, column=1)

    Label(menuframe, text="学分").grid(row=3, column=0)
    ccredit = Entry(menuframe)
    ccredit.grid(row=3, column=1)

    Button(menuframe, text="确定",
               command=lambda: update_CourseInfo_button(cno.get(), cname.get(), cpno.get(), ccredit.get())).grid(row=5,
                                                                                                                  column=1)
#
# 删除无选课的课程信息
def delete_Course_button():
    a = tkinter.messagebox.askokcancel('提示', '您确定要删除吗')
    if a == True:
        cursor = cnx.cursor()
        query = "delete from course where cno not in (select distinct cno from sc )"
        try:
            cursor.execute(query)
        except sqlc.Error:
            tkinter.messagebox.showinfo('提示', '删除失败！')
            show_menu_StuInfoModify()
            return False
        tkinter.messagebox.showinfo('提示', '删除成功！')
    cnx.commit()
    show_menu_CouInfoModify()
#ok
def delete_Course():
    menuframe = Frame(root)
    menuframe.place(rely=.4, relx=0.4, x=-122.5,y=-100, width=500, height=400)
    cursor = cnx.cursor()
    # 显示全部未选课的课程信息
    query = "select * from course where cno not in (select distinct cno from sc )"
    cursor.execute(query)
    ret="下面是全部未被选课的课程信息\n"
    ret += '%s\t%s\t%s\t%s\n' % ('Cno', 'Cname', 'Cpno', 'Ccredit')
    for (Cno, Cname, Cpno, Ccredit) in cursor:
        ret += '%s\t%s\t%s\t%s\n' % (Cno, Cname, Cpno, Ccredit)
    w1 = Message(menuframe, text=ret, width=500).grid(row=0,column=0)
    Button(menuframe, text="删除",
               command=delete_Course_button).grid(row=1, column=0)
# 插入学生成绩

def insert_Grade_button(sno, cno, grade):
    cursor = cnx.cursor()
    query = "insert into sc values('%s', '%s', '%s')" \
            % (sno, cno, grade)
    try:
        cursor.execute(query)
    except sqlc.Error:
        tkinter.messagebox.showinfo('失败', '该学生成绩插入失败！')
        show_menu_GradeModify()
        return False
    tkinter.messagebox.showinfo('成功', '该学生成绩插入成功！')
    cnx.commit()
    show_menu_GradeModify()
def insert_Grade():
    menuframe = Frame(root)
    menuframe.place(rely=.4, relx=0.4, x=-122.5,y=-100, width=500, height=400)
    Label(menuframe, text="学号").grid(row=0, column=0)
    sno = Entry(menuframe)
    sno.grid(row=0, column=1)
    Label(menuframe, text="课程号").grid(row=1, column=0)
    cno = Entry(menuframe)
    cno.grid(row=1, column=1)
    Label(menuframe, text="成绩").grid(row=2, column=0)
    grade = Entry(menuframe)
    grade.grid(row=2, column=1)
    Button(menuframe, text="确定",
               command=lambda: insert_Grade_button(sno.get(), cno.get(), grade.get())).grid(row=3,column=1)

#
# 修改学生成绩
def update_Grade_button(sno, cno, grade):
    try:
        if len(grade):
            cursor = cnx.cursor()
            query = "update sc set grade = '%s' where sno = '%s' and cno='%s'" % (grade, sno,cno)
            cursor.execute(query)
            cursor.close()
    except sqlc.Error:
        tkinter.messagebox.showinfo('修改失败', '该学生成绩修改失败！')
        show_menu_GradeModify()
        return False
    ret = '%s\t%s\t%s\n' % (sno, cno, grade)
    tkinter.messagebox.showinfo('修改成功', '该学生成绩修改后如下：\n'+ret)
    cnx.commit()
    show_menu_GradeModify()
#ok
def update_Grade():
    menuframe = Frame(root)
    menuframe.place(rely=.4, relx=0.4, x=-122.5,y=-100, width=500, height=400)
    Label(menuframe, text="学号").grid(row=0, column=0)
    sno = Entry(menuframe)
    sno.grid(row=0, column=1)
    Label(menuframe, text="课程号").grid(row=1, column=0)
    cno = Entry(menuframe)
    cno.grid(row=1, column=1)
    Label(menuframe, text="成绩").grid(row=2, column=0)
    grade = Entry(menuframe)
    grade.grid(row=2, column=1)
    Button(menuframe, text="确定",
               command=lambda: update_Grade_button(sno.get(), cno.get(), grade.get())).grid(row=3, column=1)


# 统计学生平均成绩、最高分、最低分、优秀率、不及格人数
def analysis_StudentGrade():
    cursor = cnx.cursor()
    depts=[]
    total=[]
    good=[]
    bad=[]
    menuframe = Frame(root)
    menuframe.place(rely=.4, relx=0.4, x=-160.5, y=-120, width=500, height=400)
    ret="各系平均成绩，最高分，最低分：\n"
    query = " select sdept,avg(grade) as avgg,max(grade) as maxx,min(grade) as minn from sc,student where student.sno=sc.sno group by sdept"
    cursor.execute(query)
    ret += '%s\t%s\t%s\t%s\n' % ("Sdept", "AvgGrade", "MaxGrade", "MinGrade")
    for (sdept, avgg, maxx, minn) in cursor:
        ret += '%s\t%s\t%s\t%s\n' % (sdept, avgg, maxx, minn)
    w1 = Message(menuframe, text=ret, width=500).grid(row=0, column=0,sticky=NW)
    query = "select sdept,count(*) as cn from sc,student where sc.sno=student.sno group by sdept"
    cursor.execute(query)
    for (sdept,cn) in cursor:
        depts.append(sdept)
        total.append(float(cn))

    query="select sdept,count(*) as cn from sc,student where sc.sno=student.sno and grade>=90 group by sdept"
    cursor.execute(query)
    #sdept=[]
    for (sdept,cn) in cursor:
       # sdept.append(str(sdept))
        good.append(float(cn))
    ret="各系优秀率：\nSdept\tRate\n"
    for i in range(len(depts)):
        if total[i]>0 :
            tmp=(good[i]/total[i])*100
        else:
            tmp=0.00
        tmp=round(tmp,1)
        ret+=depts[i]+"\t"+str(tmp)+"%"+"\n"
    w2 = Message(menuframe, text=ret, width=500).grid(row=1, column=0,sticky=NW)
    query = "select sdept,count(*) as cn from sc,student where sc.sno=student.sno and grade<60 group by sdept"
    cursor.execute(query)
    depts2 = []
    for (sdept, cn) in cursor:
       # print(sdept)
        depts2.append(sdept)
        bad.append(cn)
    ret="各系不及格人数：\nSdept\tNumber\n"
    for i in range(len(depts2)):
        ret+=depts2[i] + "\t" + str(bad[i])+"\n"
    w2 = Message(menuframe, text=ret, width=500).grid(row=2, column=0,sticky=NW)
    Button(menuframe, text="返回上一级",
               command=show_menu).grid(row=3, column=0)
def StuRank():
    menuframe = Frame(root)
    menuframe.place(rely=.4, relx=0.4, x=-200.5, y=-160, width=500, height=700)
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
        cursor.execute(query)
        ret+="\n%s\n"%(depts[i])
        ret += '%s\t%s\t%s\t\n' % ("Sno", "Cno", "Grade")
        for (sno,cno,grade) in cursor:
            ret += '%s\t%s\t%s\n' % (sno,cno,grade)
    w1 = Message(menuframe, text=ret, width=500).grid(row=0, column=0, sticky=NW)
    Button(menuframe, text="返回上一级",
               command=show_menu).grid(row=1,column=0)



root = Tk()
root.title("学生信息管理系统")
winWidth = 600
winHeight = 700
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

x = int((screenWidth - winWidth) / 2)
y = int((screenHeight - winHeight) / 2)
root.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
#root.resizable(False, False)

frame = Frame(root)
frame.place(rely=.5, relx=0.5, x=-122.5,y=-100, width=245, height=200)
# 返回参数信息
Label(frame, text="用户名").grid(row=0,column=0)
Label(frame, text="密码").grid(row=1,column=0)
inusername=Entry(frame)
inusername.grid(row=0,column=1)
inpwd=Entry(frame,show="*")
inpwd.grid(row=1,column=1)
Button(frame, text="登录", command=login).grid(row=2, columnspan=3)
root.mainloop()
