FROM python:3

# 安装 jupyterlab
RUN python -m pip install requests
RUN python -m pip install flask

# 暴露端口号
EXPOSE 12001

#  运行 jupyterlab
CMD python Core.py