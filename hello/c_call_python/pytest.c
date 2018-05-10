#include <Python.h>

//导出当前环境变量
void getcurrent()
{
	PyRun_SimpleString("import sys");
	PyRun_SimpleString("sys.path.append('./')");

	return ;
}

void test()
{
	Py_Initialize();//初始化pyhton
	PyRun_SimpleString("print('hello python')");//直接运行python代码
	Py_Finalize();//释放python

	return;
}

//调用模块中的一个普通函数
/*
先引用模块（PyImport_ImportModule）
然后获取模块中的函数（PyObject_GetAttrString）
对c传入python 的参数做类型转换（Py_BuildValue("(s)","hello_python")）
最后直接调用函数并传递参数（PyEval_CallObject）
-
*/
void test1()
{
	
	Py_Initialize();//初始化python
	getcurrent();

	PyObject * pModule = NULL,*pFunc= NULL, *pArg = NULL;

	pModule = PyImport_ImportModule("demo");//引入模块
				printf("<%s,%d>!\n",__FUNCTION__,__LINE__);

	pFunc = PyObject_GetAttrString(pModule,"print_arg"); //直接获取模块中的函数
				printf("<%s,%d>!\n",__FUNCTION__,__LINE__);

	pArg = Py_BuildValue("(s)","hello_python");//参数类型转换，传递一个字符串。将c/c++类型的字符串转换为python类型
				printf("<%s,%d> !\n",__FUNCTION__,__LINE__);

	PyEval_CallObject(pFunc,pArg);//调用直接获取的函数，并传递参数
				printf("<%s,%d> !\n",__FUNCTION__,__LINE__);

	Py_Finalize();//释放python
	
	return ;
}


//调用模块中的一个函数(多参数，带返回值)
void test2()
{
	Py_Initialize();
	getcurrent();
	
	PyObject * pModule = NULL,*pDict = NULL,*pFunc = NULL,*pArg  = NULL,*result=NULL;
	pModule = PyImport_ImportModule("demo"); //引入模块;
				printf("<%s,%d>!\n",__FUNCTION__,__LINE__);

	pDict = PyModule_GetDict(pModule); //获取模块字典属性 //相当于Python模块对象的 __dict__ 属性，得到模块名称空间下的字典对象  
				printf("<%s,%d>!\n",__FUNCTION__,__LINE__);

	pFunc = PyDict_GetItemString(pDict, "add"); //从字典属性中获取函数
				printf("<%s,%d>!\n",__FUNCTION__,__LINE__);

	pArg = Py_BuildValue("(i, i)", 1, 2); //参数类型转换，传递两个整型参数
				printf("<%s,%d>!\n",__FUNCTION__,__LINE__);

	result = PyEval_CallObject(pFunc, pArg); //调用函数，并得到python类型的返回值
	int sum;
				printf("<%s,%d>!\n",__FUNCTION__,__LINE__);

	PyArg_Parse(result, "i", &sum); //将python类型的返回值转换为c/c++类型

	printf("sum=%d\n", sum);
	Py_Finalize();
}

/*
//调用模块中简单的一个类（单个返回值）
void test3()
{
	Py_Initialize();
	getcurrent();
	
	PyObject *pModule = NULL, *pDict = NULL, *pClass = NULL, *pInstance = NULL, *result = NULL;
	pModule = PyImport_ImportModule("demo"); //引入模块
	pDict = PyModule_GetDict(pModule); //获取模块字典属性
	pClass = PyDict_GetItemString(pDict, "Class_A"); //通过字典属性获取模块中的类
	pInstance = PyInstance_New(pClass, NULL, NULL);//实例化获取的类
	result = PyObject_CallMethod(pInstance, "fun", "(s)", "python_000"); //调用类的方法
	char* name=NULL; 
	PyArg_Parse(result, "s", &name); //将python类型的返回值转换为c/c++类型 
	printf("%s\n", name);
	Py_Finalize();
}

//调用模块中一个简单的类（返回值是个元组）
void test4()
{
    Py_Initialize();
    getcurrent();

    PyObject *pModule = NULL, *pDict = NULL,*pClass = NULL, *pInstance = NULL, *result = NULL;
    pModule =PyImport_ImportModule("demo"); //引入模块
    pDict = PyModule_GetDict(pModule); //获取模块字典属性
    pClass = PyDict_GetItemString(pDict,"dedecms_get_webshell"); //通过字典属性获取模块中的类
    pInstance = PyInstance_New(pClass, NULL,NULL);
    result = PyObject_CallMethod(pInstance,"check", "(s,i)", "www.baidu.com", 80);
    int flag;
    char*content = NULL;
    PyObject *obj_content =PyDict_GetItemString(result, "content");
    content = PyString_AsString(obj_content);
    PyObject *obj_flag =PyDict_GetItemString(result, "flag");
    flag = PyInt_AsLong(obj_flag);
    printf("content: %s, flag: %d\n",content, flag);
	
    Py_Finalize();

}
*/
int main()
{
	test();
	test1();
	test2();
//	test3();
//	test4();

	return 0;
}



