FROM nvcr.io/nvidia/pytorch:24.01-py3

# Install requirements
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Fix bug in opencv-python
RUN pip uninstall -y opencv opencv-python-headless
RUN pip install --no-cache-dir opencv-python==4.8.0.74

# Download the pretrained model for English and Russian
RUN mkdir -p /root/.EasyOCR/model
RUN wget -P /root/.EasyOCR/model/ https://github.com/JaidedAI/EasyOCR/releases/download/pre-v1.1.6/craft_mlt_25k.zip
RUN wget -P /root/.EasyOCR/model/ https://github.com/JaidedAI/EasyOCR/releases/download/v1.6.1/cyrillic_g2.zip
RUN unzip /root/.EasyOCR/model/craft_mlt_25k.zip -d /root/.EasyOCR/model/
RUN unzip /root/.EasyOCR/model/cyrillic_g2.zip -d /root/.EasyOCR/model/
RUN rm /root/.EasyOCR/model/craft_mlt_25k.zip /root/.EasyOCR/model/cyrillic_g2.zip

# Set the working directory
WORKDIR /workspace
