#pragma once
#include"stdafx.h"
#include <iostream>
using namespace std;

struct point //链表节点
{
	int database[100];
	int length;
};

void Init_Sqlist(point&L)
{
	int a;

	printf("请输入要创建的元素的个数:\t");

	cin >> a;

	for (int i = 0; i < a; i++)

	{

		printf("请输入第%d个元素\t", i + 1);

		cin >> L.database[i];

		L.length++;
	}
}

void show(point&L)
{

	int i;

	printf("线性表中的元素为:\n");

	for (i = 0; i<L.length; i++)

		printf("%d\t", L.database[i]);

	printf("\n");

}