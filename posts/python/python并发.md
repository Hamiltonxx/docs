Python并发包含多线程、多进程和异步IO三块内容。我们需要掌握  
1. 用并发技术创建高性能和响应式的python应用
2. 开发多线程应用  
3. 开发能并行处理多任务的应用
4. 理解单线程里的并发模型

# Multithreading
## 多进程和多线程的差异
| Criteria | Process | Thread |
| --- | --- | --- |
| Memeory Sharing | Memory is not shared between processes | Memory is shared between threads within a process | 
| Memeory footprint | Large | Small |
| CPU-bound / IO-bound | CPU bound | IO bound |
| Starting time | Slower than a thread | Faster than a process |
| Interruptablity | Child processes are interruptible | Threads are not interruptible |
## Threading
