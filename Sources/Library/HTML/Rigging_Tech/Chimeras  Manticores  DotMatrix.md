---
tags: [html, Rigging_Tech]
---

# 🌐 Chimeras & Manticores – Dot Matrix.html

> **一句话总结**：自动分类：基于标题的初步推断

## 🔗 本地文件
- [Chimeras & Manticores – Dot Matrix.html](file:///Y:/GGbommer/Lib/Http/Chimeras%20&%20Manticores%20–%20Dot Matrix.html)
- **文件名称**：Chimeras & Manticores – Dot Matrix.html
- **资源类型**：html
- **归属分类**：绑定技术技巧
- **本地路径**：[[Chimeras & Manticores – Dot Matrix.html]]

> *注：本页面为 AI 深入解析本地 Lib 库后生成的资源智能索引。*


---
### 📄 离线网页正文（摘要/摘录）

Chimeras & Manticores – Dot Matrix

## Chimeras & Manticores

[![](https://theodox.github.io/theme/img/profile.png)](https://theodox.github.io)

# 

a blog about technical art, python, the games business, and obscurantism

# Dot Matrix

Posted on Sat 06 December 2014 in [blog](https://theodox.github.io/category/blog.html)

We started our math review with a look at the [dot product](http://techartsurvival.blogspot.com/2014/11/bagels-and-coffee-or-vector-dot-product.html), and started out by showing how dots work in a minimalist way. This time out we’ll do the same thing the most basic component of 3d math - the matrix.

[![](http://images.macworld.com/images/news/graphics/150845-apple_imagewriter_original.jpg)](http://images.macworld.com/images/news/graphics/150845-apple_imagewriter_original.jpg)

> There was a time when this was ‘computer graphics’

Once you start looking closely, you’/ll find that dot product and a matrix actually have a lot in common. As an older gentleman once told me when I proudly showed hin a 72 dpi dithered picture printed on my 1986 vintage Apple 2, *“Wait a minute… it’s all just…. dots?”*

In fact, matrix multiplication really is done just using dot products, as we’ll see shortly. However, matrices are more complicated, both in concept and execution. For that reason we’ll devote this post through how matrices work in the simplest possible way, so that it’s easy to see both the how and why of what they do. This post will be primarily about the most minimal example of how a matrix functions. I’ll do it in 2-d to keep the math a bit less wordy, though the same thing works in 3 or even more dimensions. I’ll also be sticking to a simple rotate-only matrix to start with so the workings are simple - I’ll add in translations and scales next time out to keep the focus on the basics.

## First things first

So, starting with the bare minimum, let’s suppose we’ve got a simple unit-length vector `[1,0]` and we’d like to figure out how to rotate it. Rotating that unit vector 45 degrees should end up as `[.707, .707], as you can see below:`

[![](http://freespace.virgin.net/hugo.elias/routines/rotate01.gif)](http://freespace.virgin.net/hugo.elias/routines/rotate01.gif)

> We’re trying to figure out an operation that will give these values as we rotate from [1,0] to [0,1]

*(If the numbers seem surprising, you might want to hop back to the discussion of the unit circle in our earlier [discussion of dot products](http://we%27re%20trying%20to%20figure%20out%20an%20operation%20that%20will%20give%20these%20values%20as%20we%20rotate%20from%20[1%2C0]%20to%20[0%2C1]/).)*

The question is, what kind of operations do we need to do to perform that rotation? What tools do we have to make it work - and, even more importantly, to make it work for any vector and not just this one example?

First, just to clear the decks, let’s check off things that *wont’* work.

We can see that difference between the first vector and the second is `[-.293, .707]` – but it’s pretty obvious that simple addition is not the same thing as performing a rotation. If you’re not convinced, just note that adding the same vector again will get you `[.121, 1.414]` rather than the expected `[0,1]`.

Plain old multiplication doesn’t work either - there is no number we can multiply against the original `[1,0]` that will get a non-zero result in the Y component.

So what can we do? Fortunately, our old friend the [dot product](http://techartsurvival.blogspot.com/2014/11/dots-all-folks.html) comes to the rescue. If you recall how we introduced dots, you should remember that one of the uses of the dot product is to project one vector on to another.

[![](http://gregegan.customer.netspace.net.au/ORTHOGONAL/02/004.png)](http://gregegan.customer.netspace.net.au/ORTHOGONAL/02/004.png)

So suppose what would happen if we tried to project our first vector onto another vector that looked like a rotated coordinate system. In other words, we could hold our original vector constant and ‘rotate’ the X-axis counterclockwise by 45 degrees. It’s a theory-of-relativity kind of thing: rotating our vector N degrees clockwise and rotating the world N degrees counter-clockwise are the same thing.

By projecting our X-axis against the rotated vector, though, we get the X component we want from a 45 degree angle:  
[![](http://2.bp.blogspot.com/-qbl5CZAwTN8/VH9FE9epOoI/AAAAAAABLZA/ZXbLLOU2qTU/s1600/rotate%2Bcoordfs.png)](http://2.bp.blogspot.com/-qbl5CZAwTN8/VH9FE9epOoI/AAAAAAABLZA/ZXbLLOU2qTU/s1600/rotate%2Bcoordfs.png)

> Rotating a vector (left) is the same as counter-rotating the coordinate system (right)

We can use the [unit circle](https://www.blogger.com/link) (or the chart of angle values above) to figure out what the right vector for the counter rotated X-axis is. In the rotated-X-axis world we will be dotting `[1,0]` against the vector `[.707, -.707]`. Drawing on what know from [last time](http://techartsurvival.blogspot.com/2014/11/bagels-and-coffee-or

... (原文过长，已截断)