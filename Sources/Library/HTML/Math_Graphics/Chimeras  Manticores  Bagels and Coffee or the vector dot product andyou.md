---
tags: [html, Math_Graphics]
---

# 🌐 Chimeras & Manticores – Bagels and Coffee, or, the vector dot product and you.html

> **一句话总结**：自动分类：基于标题的初步推断

## 🔗 本地文件
- [Chimeras & Manticores – Bagels and Coffee, or, the vector dot product and you.html](file:///Y:/GGbommer/Lib/Http/Chimeras%20&%20Manticores%20–%20Bagels%20and%20Coffee,%20or,%20the%20vector%20dot%20product%20and you.html)
- **文件名称**：Chimeras & Manticores – Bagels and Coffee, or, the vector dot product and you.html
- **资源类型**：html
- **归属分类**：数学与图形学
- **本地路径**：[[Chimeras & Manticores – Bagels and Coffee, or, the vector dot product and you.html]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 离线网页正文（摘要/摘录）

Chimeras & Manticores – Bagels and Coffee, or, the vector dot product and you

## Chimeras & Manticores

[![](https://theodox.github.io/theme/img/profile.png)](https://theodox.github.io)

# 

a blog about technical art, python, the games business, and obscurantism

# Bagels and Coffee, or, the vector dot product and you

Posted on Sat 22 November 2014 in [blog](https://theodox.github.io/category/blog.html)

I’ve been boning up on my math lately.

Like most TA’s I’ve cobbled together a bag of tricks from different situations I’ve dealt with over the years, but I’ve never really gone back to shore up my shaky high school trigonometry and pre-calculus. It’s certainly possible (at least, I hope it is!) to be a good TA with only seat-of-the-pants math skills — after all, we have parenting and scaling and all the other cool tricks in our apps to do the heavy lifting for us. Still, I’ve been finding that paying more attention to the math fundamentals is helping me solve problems more efficiently and elegantly than my patented hack-and-slash techniques did.  
So, I’m starting an occasional series on some basic math concepts that I hope will be useful to other TA’s. I know it’s been helpful to me - there’s nothing that concentrates the mind like putting something out there on the internet for public commentary - it’s really forces you to think things through… *At least, as long as you’re not on Twitter*.

To kick off the series, I want to start off with a simple operation that I use all the time, the humble [dot product](http://en.wikipedia.org/wiki/Dot_product). Also known as the ‘scalar’ product, the dot is an operation for turning lists of numbers into a single number. It’s also astonishingly useful for graphics. I’ve used it for years, but only recently did I try to see how and *why* it works instead of just relying on the second-hand assurance *that* it works.

The dot is all about combining operations on lists. We always run into it in the context of geometric vectors, but in the pure math world vector is just another way of saying “list of similar numbers.” If you go to the coffee shop every day and buy a $5 latte, its obviously going to cost $25 a week (Tote that up over 48 work weeks a year - it’s a lot of money! I bring instant. But I digress). If you buy a $2 bagel on monday and a $3 cookie on Wednesday and Friday, how much will it cost?:

```
5 * 5 = $25 for coffee  
2 * 1 = $2 for bagel  
3 * 2 = $6 for cookies
```

This makes $33 total a week (you really should bring in your snacks from home. You’ll save a ton!)

Besides helping you save money on lunch, this is a classic (though non-3-d related) example of the dot product in action. Dots are nothing more than a structured way of multiplying two lists of numbers. In this case we have list of prices:

```
[5, 2, 3]
```

and a list of quantities:

```
[5, 1, 2]
```

The dot operation merely multiplies the numbers in the same position in the list and adds them together. As you can see, this is trivial math:

```
(5 * 5) +  (2 * 1) + (3 * 2)
```

Despite it’s humble origins, however, this trick — multiplying ordered pairs of numbers and adding them up - is absolutely basic in 3-D graphics. The lists of prices and quantities become vectors (in fact, general purpose algebra calls any list a ‘vector’) and with a simple convention the dot product takes on a very interesting and useful set of properties for TA’s to exploit.  
The most famous example of the dot product in graphics is [the original Lambert shading equation](http://en.wikipedia.org/wiki/Lambertian_reflectance):

```
N dot L
```

Where N is a surface normal and L is the angle of the incident light.

[![](http://upload.wikimedia.org/wikipedia/commons/thumb/0/03/VisualPhotometry_Fig2_from_Lambert'sPhotometria.jpg/2880px-VisualPhotometry_Fig2_from_Lambert'sPhotometria.jpg)](http://upload.wikimedia.org/wikipedia/commons/thumb/0/03/VisualPhotometry_Fig2_from_Lambert'sPhotometria.jpg/2880px-VisualPhotometry_Fig2_from_Lambert'sPhotometria.jpg)

> The ‘Lambert shader’ is based on this math textbook from 1760. How cool is that?

Lambertian shading is probably the single most common operation in computer graphics, but it’s the same math as figuring out your coffee budget. Here’s how the magical translation from bagels and coffee to shaded pixels works:  
Imagine a sphere being lit by a directional light from straight above, in classic CG fashion. The vector to the light would be

```
[0, 0, 1]
```

On top of the sphere, the normal vector would point the same way - it too would point up towards

```
[0, 0, 1]
```

The dot of these two is:

```
(0 * 0) + (0 * 0) + (1 * 1)
```

in other words, 1. This makes sense: our light is directly overhead, so the sample point on top of the sphere receives the full incoming light. Compare this to a point halfway down the sphere. A a normal point 45 degrees from the vertical might be

```
[.707, 0, .707]
```

And the dot would be

```
(0 *.707) + (0 * 0) + (1 * .707)
```

or

... (原文过长，已截断)