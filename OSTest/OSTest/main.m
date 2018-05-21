//
//  main.m
//  OSTest
//
//  Created by shilei on 2018/5/20.
//  Copyright © 2018年 shilei. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "TestClass.h"
int main(int argc, const char * argv[]) {
    @autoreleasepool {
        // insert code here...
        NSLog(@"Hello, World!");
        [TestClass staticFun];
        TestClass *theClass =[[TestClass alloc]init];
        [theClass print:@"1111":@"22222"];
        NSLog(@"%d",[theClass Compare: 1 : 1]);
        Circle* circle = [Circle new];
        [circle method2];
        
        Shape shapes[3];
        ShapeRect rect0 = {0,0,10,30};
        //枚举直接？？？
        shapes[0].type =  kCircle;
        shapes[0].fillColor = kRedColor;
        shapes[0].bounds = rect0;
        
        ShapeRect rect1 = {30,40,50,60};
        shapes[1].type = kRectangle;
        shapes[1].fillColor = kGreenColor;
        shapes[1].bounds = rect1;
        
        ShapeRect rect2 = {15,18,37,29};
        shapes[2].type = kEgg;
        shapes[2].fillColor = kBlueColor;
        shapes[2].bounds = rect2;
        
        
        
    }
    return 0;
}

//面向过程的函数调用有先后顺序

NSString* colorName(ShapeColor fillColor)
{
    switch (fillColor) {
            
        case kRedColor:
            return @"red";
            break;
        case kBlueColor:
            return @"blue";
            break;
        case kGreenColor:
            return @"green";
            break;
        default:
            return @"No Color";
            break;
    }
    return @"No Color";
}
void drawCircle(ShapeRect bounds,ShapeColor fillColor)
{
    NSLog(@"drawing a circle at(%d,%d,%d,%d) in %@",bounds.x,bounds.y,bounds.height,bounds.width,colorName(fillColor));
}

void drawShapes(Shape shapes[],int count)
{
    
    //    for (int i=0;i<count;i++) {
    //        switch (shapes[i].type) {
    //            case kCircle:
    //                dra
    //                break;
    //
    //            default:
    //                break;
    //        }
    //    }
}


