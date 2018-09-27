#pragma once
#include"stdafx.h"


void quick_writer(int L[] , int a,int &Length)
{
	//数组快速输入函数,顺序数字填入数组内部
	for (int i = 0; i < a; i++)
	{
		//快速赋值函数
		L[i] = i + 1;
		Length++;
	}
}

void copy_array(int a[],int a_i,int b[])
{
	for (int i = 0; i < a_i; i++)
	{
		a[i] = b[i];

	}
}