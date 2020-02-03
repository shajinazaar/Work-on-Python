{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "PermissionError",
     "evalue": "[Errno 13] Permission denied: 'C:\\\\Windows\\\\System32\\\\drivers\\\\etc\\\\hosts'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mPermissionError\u001b[0m                           Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-fc909431a3aa>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m     23\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     24\u001b[0m     \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 25\u001b[1;33m         \u001b[1;32mwith\u001b[0m \u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mhost_path\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'+r'\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mfile\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     26\u001b[0m             \u001b[0mcontent\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfile\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mreadlines\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     27\u001b[0m             \u001b[0mfile\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mseek\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mPermissionError\u001b[0m: [Errno 13] Permission denied: 'C:\\\\Windows\\\\System32\\\\drivers\\\\etc\\\\hosts'"
     ]
    }
   ],
   "source": [
    "import time\n",
    "from datetime import datetime as dt\n",
    "\n",
    "host_temp=\"hosts\"\n",
    "host_path=r\"C:\\Windows\\System32\\drivers\\etc\\hosts\"\n",
    "redirect =\"127.0.0.1\"\n",
    "website_list=[\"www.facebook.com\",\"facebook.com\",\"outlook.live.com/mail/inbox\",\"www.outlook.live.com/mail/inbox\"]\n",
    "\n",
    "year =dt.now().year\n",
    "month=dt.now().month\n",
    "day=dt.now().day\n",
    "\n",
    "while True:\n",
    "    if dt(year,month,day,8) < dt.now() < dt(year,month,day,15):\n",
    "        print(\"Working hour...\")\n",
    "        with open(host_temp,\"r+\") as file:\n",
    "            content = file.read()\n",
    "            for website in website_list:\n",
    "                if website in content:\n",
    "                    pass\n",
    "                else:\n",
    "                    file.write(redirect + \" \" + website + \"\\n\")                   \n",
    "    \n",
    "    else:\n",
    "        with open(host_temp,'+r') as file:\n",
    "            content = file.readlines()\n",
    "            file.seek(0)\n",
    "            for lines in content:\n",
    "                if not any(website in lines for website in website_list):\n",
    "                    file.write(lines)\n",
    "            file.truncate()\n",
    "        print(\"Fun hour\")\n",
    "    time.sleep(5)\n",
    "        \n",
    "    \n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
