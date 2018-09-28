#pragma once
#include "stdafx.h"
#include <iostream> 
#include <string>
using namespace std;

struct list
{
	char name[20];
	char sex[5];
	int number;
	list *next = NULL;
	list *back = NULL;//双向列表,存在两个方向
};

list * list_init(int n)
{
	//创建m个节点
	list *p1, *p2, *head;
	head = new list;
	head->back = NULL;
	//此处是为了给头指针赋值,使得p1->back有指针方向,从而使得倒序输出得以实现
	p1 = new list;
	p1->back = head;
	//NULL改为了head
	p2 = new list;
	p2->back = p1;
	head = p1;
	for (int i = 0; i < n; i++)
	{
		strcpy_s(p1->name, 5, "test");
		p1->number = i+1;
		p1->next = p2;
		p2->back = p1;
		p1 = p2;
		p2 = new list;
	}
	p2->next = NULL;
	p2->back = p1;
	return head;
}

void show_list(list *head)
{
	list *p1; int i=0;//节点数量标志量
	p1 = head;
	while (p1->next != NULL && head != NULL)
	{
		cout << p1->name << ' ' << p1->number << endl;
		p1 = p1->next;
		i++;
	}
	cout << "back show " << i << endl;
	/*p1 = p1->back;
	while (p1->back != NULL && head != NULL)
	{
		cout << p1->name << ' ' << p1->number << endl;
		p1 = p1->back;
	}
	cout << p1->name << ' ' << p1->number << endl;*/
	//由于p1->back是NULL,所以无法执行循环,因此在后续处加入一行代码输出p1
	//下面更改为for循环倒序输出
	p1 = p1->back;
	for (int j = 0; j < i&&p1->back!=NULL; i++)
	{
		cout << p1->name << ' ' << p1->number << endl;
		p1 = p1->back;
	}
	//这样只能输出后面的4个值
	//更改前面的头指针head
}