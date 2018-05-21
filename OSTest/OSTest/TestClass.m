//
//  TestClass.m
//  OSTest
//
//  Created by shilei on 2018/5/20.
//  Copyright © 2018年 shilei. All rights reserved.
//

#import <Foundation/Foundation.h>
#include "TestClass.h"

@implementation TestClass

-(void) print:(NSString*)str1 :(NSString*)str2{
    NSLog(@"this is a test for print");
    NSLog(@"%@",str1);
    NSLog(@"%@",str2);
}

+(void) staticFun{
    NSLog(@"this is a static method of the class");
}

-(BOOL) Compare:(int)intagerA :(int)intargerB{
    if(intagerA==intargerB)
        return YES;
    else
        return NO;
}
@end


@implementation Circle
-(void) method1:(int)param
{
    NSLog(@"this is number:%d",param);
}
-(void) method2
{
    NSLog(@"this is method of circle");
}
@end
