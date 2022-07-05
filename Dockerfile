FROM python:3.10-bullseye

RUN useradd --create-home --shell /bin/bash general_user

WORKDIR /home/general_user/app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN chown -R general_user:general_user /home/general_user/app

USER general_user

COPY . .

CMD ["bash"]