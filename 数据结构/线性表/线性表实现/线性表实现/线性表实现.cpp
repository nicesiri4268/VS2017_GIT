// 线性表实现.cpp: 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include "Sq_list.h"
#include <stdio.h>
#include <iostream>
using namespace std;

int main()
{
	using namespace std;
	sqlist L;
	Init_Sqlist(L);//构建线性表,返回线性表的地址
	show(L);
	cout << listempty(L) << endl;
	int e;
	getElem(L, 2, e);
	cout << e << endl;
	cout << listlength(L) << endl;
	getchar();//暂停程序等待输入
    return 0;
}

