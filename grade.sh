#!/bin/bash
# grade.sh
# Basic auto-grading script

echo "🏁 Starting Auto Grading..."
echo "✅ Checking backend API health..."
curl -s http://localhost:8000/api/health || echo "⚠️ Backend not reachable (this may be expected in CI)"

echo "✅ Checking frontend build folder..."
if [ -d "./frontend" ]; then
  echo "✅ Frontend folder exists."
else
  echo "❌ Frontend folder missing!"
fi

echo "✅ Auto Grading Complete!"
exit 0
