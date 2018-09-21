#pragma once
#include"stdafx.h"
#include <iostream>
using namespace std;

struct point //链表节点
{
	int *elem;
	int base_size = 5;
	int add_long = 5;
	int length;
	int database_long;
};

void Init_Sqlist(point&L)
{
	int a;

	printf("请输入要创建的元素的个数: ");
	cin >> a;

	//L.elem = (int *)malloc(L.base_size * sizeof(int));//传统方法申请数量表
	L.elem = new int[a];//new申请一个空间的话不需要名称直接写大小,即new int [20],而不是new int A[20];

	/*for (int i = 0; i < a; i++)
	{
			printf("请输入第%d个元素\t", i + 1);
			cin >> L.elem[i];
			L.length++;
	}*/
	for (int i = 0; i < a; i++)
	{
		//快速赋值函数
		L.elem[i] = i+1;
		L.length++;
	}
	
}

void show(point&L)
{

	int i;

	printf("线性表中的元素为:\n");

	for (i = 0; i<L.length; i++)

		printf("%d\t", L.elem[i]);

	printf("\n");

}