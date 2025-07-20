#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para agregar datos de muestra al sistema de gestión de videos
"""

import sqlite3
from datetime import datetime, timedelta

def add_sample_data():
    """Agregar videos de muestra a la base de datos"""
    
    # Conectar a la base de datos
    conn = sqlite3.connect('video_management.db')
    cursor = conn.cursor()
    
    # Datos de muestra
    sample_videos = [
        {
            'title': 'Video Tutorial 1',
            'description': 'Tutorial básico sobre el uso del sistema',
            'google_drive_url': 'https://drive.google.com/file/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/view',
            'expiry_date': (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d %H:%M:%S'),
            'allow_download': 1,
            'view_count': 45
        },
        {
            'title': 'Video Tutorial 2',
            'description': 'Tutorial avanzado con funciones especiales',
            'google_drive_url': 'https://drive.google.com/file/d/1abc123def456ghi789jkl012mno345pqr678stu901vwx/view',
            'expiry_date': (datetime.now() + timedelta(days=15)).strftime('%Y-%m-%d %H:%M:%S'),
            'allow_download': 0,
            'view_count': 63
        },
        {
            'title': 'Video Demo Expirado',
            'description': 'Este video ha expirado para demostrar la funcionalidad',
            'google_drive_url': 'https://drive.google.com/file/d/1xyz987wvu654tsr321qpo098nml765kji432hgf210edc/view',
            'expiry_date': (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S'),
            'allow_download': 1,
            'view_count': 28,
            'is_archived': 0
        }
    ]
    
    # Insertar videos de muestra
    for video in sample_videos:
        cursor.execute('''
            INSERT INTO videos (title, description, google_drive_url, expiry_date, allow_download, view_count, is_archived, upload_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            video['title'],
            video['description'], 
            video['google_drive_url'],
            video['expiry_date'],
            video['allow_download'],
            video['view_count'],
            video.get('is_archived', 0),
            datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ))
    
    # Confirmar cambios
    conn.commit()
    conn.close()
    
    print("✅ Datos de muestra agregados exitosamente!")
    print("📋 Se agregaron {} videos de muestra".format(len(sample_videos)))
    print("🌐 Ahora puede ver la interfaz completa en español")

if __name__ == '__main__':
    add_sample_data()
