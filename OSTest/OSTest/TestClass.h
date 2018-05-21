//
//  TestClass.h
//  OSTest
//
//  Created by shilei on 2018/5/20.
//  Copyright © 2018年 shilei. All rights reserved.
//

#ifndef TestClass_h
#define TestClass_h
@interface TestClass:NSObject
+(void)staticFun;
-(void)print:(NSString*)str1 :(NSString*) str2;
-(BOOL)Compare:(int)intagerA :(int)intargerB;
@end


@interface Circle:NSObject
{
@private
    int firstAttr;
    float secondAttr;
}
-(void)method1:(int) param;
-(void)method2;
@end

typedef enum{
    kCircle,
    kRectangle,
    kEgg
}ShapeType;

typedef enum{
    kRedColor,
    kGreenColor,
    kBlueColor
} ShapeColor;

typedef struct{
    int x,y,width,height;
}ShapeRect;

typedef struct{
    ShapeType type;
    ShapeColor fillColor;
    ShapeRect bounds;
}Shape;

#endif /* TestClass_h */
