#!/bin/bash

# Script para deploy no Google Cloud Run

# Variáveis de configuração
PROJECT_ID="seu-project-id"
SERVICE_NAME="terapia-mvp"
REGION="us-central1"
IMAGE_NAME="gcr.io/$PROJECT_ID/$SERVICE_NAME"

echo "🚀 Iniciando deploy no Google Cloud Run..."

# 1. Verificar se o gcloud está configurado
echo "📋 Verificando configuração do gcloud..."
gcloud config get-value project

# 2. Habilitar APIs necessárias
echo "🔧 Habilitando APIs..."
gcloud services enable cloudbuild.googleapis.com
gcloud services enable run.googleapis.com

# 3. Build da imagem
echo "🏗️ Construindo imagem Docker..."
gcloud builds submit --tag $IMAGE_NAME

# 4. Deploy no Cloud Run
echo "🚀 Fazendo deploy no Cloud Run..."
gcloud run deploy $SERVICE_NAME \
    --image $IMAGE_NAME \
    --platform managed \
    --region $REGION \
    --port 8080 \
    --memory 1Gi \
    --cpu 1 \
    --min-instances 0 \
    --max-instances 10 \
    --allow-unauthenticated \
    --set-env-vars "GOOGLE_API_KEY=$GOOGLE_API_KEY"

echo "✅ Deploy concluído!"
echo "🌐 Sua aplicação está disponível em:"
gcloud run services describe $SERVICE_NAME --platform managed --region $REGION --format 'value(status.url)'
