#pragma once
#include"stdafx.h"
#include <iostream>
#include"备用函数.h"

using namespace std;

struct sqlist //链表节点
{
	int *elem;//顺序表链的数组指针,初始化指针为(整型变量)
	int base_size = 5;//线性表的初始化空间
	int add_long = 5;//线性表的空间不够后的需加值
	int length = 0;//线性表的长度

};

void Init_Sqlist(sqlist&L)
{
	//L.elem = (int *)malloc(L.base_size * sizeof(int));//传统方法申请数量表
	L.elem = new int[L.base_size];//new申请一个空间的话不需要名称直接写大小,即new int [20],而不是new int A[20];
	//创建一个空的顺序线性表
	int a = 5;//测试用的数值
	/*for (int i = 0; i < a; i++)
	{
			printf("请输入第%d个元素\t", i + 1);
			cin >> L.elem[i];
			L.length++;
	}*/

	quick_writer(L.elem,a,L.length);
}

void show(sqlist&L)
{
	//展示所有节点的数据元素
	int i;

	printf("线性表中的元素为:\n");

	for (i = 0; i<L.length; i++)

		printf("%d\t", L.elem[i]);

	printf("\n");

}

void destory(sqlist &L)
{
	//销毁线性表
	delete[]L.elem;//释放内存空间
	L.elem = NULL;
}

void clear_sqlist(sqlist&L)
{
	//清空线性表,无论是否为空,全部重置为
	L.length = 0;
}

bool listempty(sqlist&L)
{
	//判断线性表是否为空,为空是返回true(1),否则false(0)
	if (L.length == 0)return true;
	else return false;
}

int listlength(sqlist&L)
{
	//返回线性表中元素个数
	return L.length;
}

bool getElem(sqlist&L,int i,int &e)
{
	//返回线性表中的第i个数据元素的值,使用(e)返回,函数返回值为true或false
	if (i <= L.length)
	{
		e = L.elem[i - 1];
		return true;
	}
	else
		return false;
}

bool listInsert(sqlist &L, int i, int &e)
{
	//插入节点,需要区分节点的位置,(1)空间已经满,需要重新分配空间//
	//if (L.length)
	//int *a;
	//a = new int [L.length];//新建一个数组,用于储存原数组
	//copy_array(a, L.length, L.elem);
	//if ()
	//暂时不知道如何获取数组是否为满数组
	return true;
}