html = f"""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
            <title>BitNBuild Hackathon</title>
            <style>
                body {{
                    font-family: 'Roboto', sans-serif;
                    color: #202124;
                    background-color: #f1f3f4;
                    margin: 0;
                    padding: 0;
                }}
                .container {{
                    background-color: #ffffff;
                    margin: 40px auto;
                    padding: 32px;
                    max-width: 600px;
                    border-radius: 8px;
                    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                    border: 1px solid #e0e0e0;
                }}
                .logo {{
                    text-align: center;
                    margin-bottom: 5px;
                }}
                .logo img {{
                    width: 130px;
                    opacity: 0.9;
                }}
                h2 {{
                    font-size: 26px;
                    color: #1a73e8;
                    font-weight: 500;
                    margin-top: 0;
                    text-align: left;
                    margin-bottom: 20px;
                }}
                p {{
                    font-size: 16px;
                    line-height: 1.7;
                    color: #5f6368;
                    margin-bottom: 15px;
                }}
                a {{
                    color: #1a73e8;
                    text-decoration: none;
                    font-weight: 500;
                }}
                .button {{
                    display: inline-block;
                    padding: 10px 20px;
                    background-color: #1a73e8;
                    color: white;
                    text-decoration: none;
                    border-radius: 6px;
                    font-weight: 500;
                    text-align: center;
                    transition: background-color 0.3s ease;
                }}
                .button:hover {{
                    background-color: #155db3;
                }}
                .highlight {{
                    background-color: #f1f3f4;
                    border-left: 5px solid #c4c4c4;
                    padding: 16px;
                    border-radius: 4px;
                    font-size: 15px;
                    margin-top: 20px;
                    color: #666;
                }}
                .highlight p {{
                    margin: 0;
                }}
                .footer {{
                    margin-top: 30px;
                    font-size: 14px;
                    color: #9e9e9e;
                    text-align: left;
                    border-top: 1px solid #e0e0e0;
                    padding-top: 20px;
                }}
                .footer strong {{
                    color: #5f6368;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="logo">
                    <img src="https://i.imgur.com/gEaH6w2.png" alt="GDG Logo">
                </div>
                <h2>Dear {participant_name},</h2>
                <p>Thank you for showing interest and registering for the <strong>Bit N Build Hackathon</strong>! We are excited to see your enthusiasm. Here are the important details for the event:</p>
                <p><strong>Date:</strong> 3rd October<br/><strong>Timings:</strong> 9:00 AM - 4:00 PM<br/><strong>Venue:</strong> C325</p>
                <p>For updates and to receive the problem statements and other key details, please join our Telegram group:</p>
                <a href="https://t.me/Bitnbuild" style="display: inline-block; padding: 10px 20px; background-color: #1a73e8; color: white; text-decoration: none; border-radius: 6px; font-weight: 500; text-align: center; transition: background-color 0.3s ease;">Join the Telegram Group</a><br>
                <p>We look forward to seeing you there and wish you all the best for the hackathon!</p>
                <div class="footer">
                    <p>Best regards,<br><strong>GDG</strong><br><strong>KL University</strong></p>
                </div>
            </div>
        </body>
    </html>
    """
